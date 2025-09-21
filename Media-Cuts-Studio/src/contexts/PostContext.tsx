// Front-end/postflow-forge/src/contexts/PostContext.tsx
import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';

export interface Post {
  id: string;
  title: string;
  description: string;
  tags: string[];
  scheduledAt: string;
  socialNetworks: string[];
  status: 'draft' | 'scheduled' | 'published' | 'error';
  createdAt: string;
  media?: {
    filename: string;
    type: 'image' | 'video';
    url: string;
  };
  visibility?: 'public' | 'private' | 'unlisted';
  canal_id: string;          // principal
  canal_id_tiktok?: string;  // novo
}

interface PostContextType {
  posts: Post[];
  fetchPosts: (filters?: { status?: string; socialNetwork?: string; searchQuery?: string; sortBy?: string; sortOrder?: string; page?: number; limit?: number }) => Promise<void>;
  addPost: (post: Omit<Post, 'id' | 'createdAt'>) => Promise<void>;
  updatePost: (id: string, updates: Partial<Post>) => Promise<void>;
  deletePost: (id: string) => Promise<void>;
  getPostsForDate: (date: string) => Post[];
  getDashboardStats: () => {
    today: number;
    week: number;
    month: number;
    draft: number;
    scheduled: number;
    published: number;
    error: number;
  };
}

const PostContext = createContext<PostContextType | undefined>(undefined);

export const usePost = () => {
  const context = useContext(PostContext);
  if (context === undefined) {
    throw new Error('usePost must be used within a PostProvider');
  }
  return context;
};

export const PostProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [posts, setPosts] = useState<Post[]>([]);

  const API_BASE_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:5000/api'; // Certifique-se de que esta variável de ambiente está configurada

  const fetchPosts = useCallback(async (filters: { status?: string; socialNetwork?: string; searchQuery?: string; sortBy?: string; sortOrder?: string; page?: number; limit?: number } = {}) => {
    try {
      const queryParams = new URLSearchParams();
      if (filters.searchQuery) queryParams.append('searchQuery', filters.searchQuery);
      if (filters.status) queryParams.append('status', filters.status);
      if (filters.socialNetwork) queryParams.append('socialNetwork', filters.socialNetwork);
      if (filters.sortBy) queryParams.append('sortBy', filters.sortBy);
      if (filters.sortOrder) queryParams.append('sortOrder', filters.sortOrder);
      if (filters.page) queryParams.append('page', String(filters.page));
      if (filters.limit) queryParams.append('limit', String(filters.limit));

      const response = await fetch(`${API_BASE_URL}/api/posts?${queryParams.toString()}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      const normalizedPosts: Post[] = data.posts.map((p: any) => ({
        ...p,
        socialNetworks: typeof p.socialNetworks === 'string'
          ? JSON.parse(p.socialNetworks)
          : Array.isArray(p.socialNetworks)
            ? p.socialNetworks
            : [],            // fallback caso venha nulo/outro tipo
      }));

      setPosts(normalizedPosts);
    } catch (error) {
      console.error("Failed to fetch posts:", error);
      // Opcional: Adicionar um estado de erro ou notificação ao usuário
    }
  }, [API_BASE_URL]);

  useEffect(() => {
    fetchPosts(); // Fetch posts on initial component mount
  }, [fetchPosts]);

  const addPost = async (postData: Omit<Post, 'id' | 'createdAt'>) => {
    try {
      const response = await fetch(`${API_BASE_URL}/posts`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      // Re-fetch posts to get the latest list including the new post
      await fetchPosts(); 
    } catch (error) {
      console.error("Failed to add post:", error);
    }
  };

  const updatePost = async (id: string, updates: Partial<Post>) => {
    try {
      const response = await fetch(`${API_BASE_URL}/posts/${id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updates),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      // Re-fetch posts to reflect the update
      await fetchPosts();
    } catch (error) {
      console.error("Failed to update post:", error);
    }
  };

  const deletePost = async (id: string) => {
    try {
      const response = await fetch(`${API_BASE_URL}/posts/${id}`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      // Re-fetch posts to reflect the deletion
      await fetchPosts();
    } catch (error) {
      console.error("Failed to delete post:", error);
    }
  };

  const getPostsForDate = useCallback((date: string) => {
    const targetDate = new Date(date);
    // Adjust targetDate to start of the day in local timezone for comparison
    targetDate.setHours(0, 0, 0, 0);

    return posts.filter(post => {
      const postScheduledDate = new Date(post.scheduledAt);
      // Adjust postScheduledDate to start of the day in local timezone for comparison
      postScheduledDate.setHours(0, 0, 0, 0);
      return postScheduledDate.toDateString() === targetDate.toDateString();
    });
  }, [posts]);

  const getDashboardStats = useCallback(() => {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const weekStart = new Date(today.getTime() - (today.getDay() * 24 * 60 * 60 * 1000));
    const monthStart = new Date(now.getFullYear(), now.getMonth(), 1);

    return {
      today: posts.filter(post => {
        const postDate = new Date(post.scheduledAt);
        return postDate >= today && postDate < new Date(today.getTime() + 24 * 60 * 60 * 1000);
      }).length,
      week: posts.filter(post => {
        const postDate = new Date(post.scheduledAt);
        return postDate >= weekStart;
      }).length,
      month: posts.filter(post => {
        const postDate = new Date(post.scheduledAt);
        return postDate >= monthStart;
      }).length,
      draft: posts.filter(post => post.status === 'draft').length,
      scheduled: posts.filter(post => post.status === 'scheduled').length,
      published: posts.filter(post => post.status === 'published').length,
      error: posts.filter(post => post.status === 'error').length
    };
  }, [posts]);

  return (
    <PostContext.Provider value={{
      posts,
      fetchPosts,
      addPost,
      updatePost,
      deletePost,
      getPostsForDate,
      getDashboardStats
    }}>
      {children}
    </PostContext.Provider>
  );
};