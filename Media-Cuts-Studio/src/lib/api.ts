
import React, { useEffect, useRef, useState  } from 'react';



export interface ScheduleConfig {
  pastedUrl: string;
  thumbnail_url: string;
  includeHorizontal: boolean;
  includeVertical: boolean;
  user_email: string;
  legendstheme: string;
  editiontheme: string;
  ytChannel: string;
  apiKey: string;
  cuttingSeconds: number[]; 
  customSettings?: Record<string, any>;
  username_account: string;
  downloadToPanelEnabled: boolean;
  customTitleEnabled: boolean;
  videoTitle: string;
  latestEnabled: boolean;
  videoTitleForLatestVideo: string;
  secondsScheduleTiktokVideo: number;
  titleForTiktokCutsEnabled: boolean;
  titleForTiktokCuts: string;
  hashtagsForTiktokCutsEnabled: boolean;
  hashtagsForTiktokCuts: string;
  ShortifyMode: string; 
}

export interface ScheduleResult {
  ytChannel: string;
  apiKey: string;
  cuttingSeconds: number[]; 
}
export interface StartShortifyPayload {
  ytChannel: string;
  cuttingSeconds: number[];
  thumbnail_url: string;
  includeHorizontal: boolean;
  includeVertical: boolean;
  user_email: string;
  legendstheme: string;
  editiontheme: string;
  apiKey: string;
  customSettings: Record<string, any>;
  username_account: string;
  downloadToPanelEnabled: boolean;
  customTitleEnabled: boolean;
  videoTitle: string;
  videoTitleForLatestVideo: string;
  latestEnabled: boolean;
  pastedUrl: string;
  secondsScheduleTiktokVideo: number;
  titleForTiktokCutsEnabled: boolean;
  titleForTiktokCuts: string;
  hashtagsForTiktokCutsEnabled: boolean;
  hashtagsForTiktokCuts: string;
  ShortifyMode: string;
}

export interface ExpandedSections {
  schedule: boolean;
  video: boolean;
  content: boolean;
  account: boolean;
  advanced: boolean;
}

export interface TaskSchedulerProps {
  ytChannel: string;
  setYtChannel: React.Dispatch<React.SetStateAction<string>>;
  apiKey: string;
  setApiKey: React.Dispatch<React.SetStateAction<string>>;
  videoUrl: string;
}

export interface Account {
  id: string;  
  platform: string;
  username: string;
  status: string;
}

export interface VideoProps {
  id: string;
  title: string;
  thumbnail: string;
}

export interface ChannelVideosResponse {
  status: string;
  channel: string;
  limit: number;
  videos: VideoProps[];
}

export interface LegendsThemeOption {
  name: string;
  gif: string;
  settings: Record<string, any>;
}

export interface ShortifyOption {
  name: string;
}
export interface EditionThemeOption {
  name: string;
}
