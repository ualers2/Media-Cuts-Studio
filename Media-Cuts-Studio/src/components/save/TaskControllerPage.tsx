// web_project\src\components\TasksPage.tsx
import React, { useEffect, useState } from 'react';
import TaskController from './TaskController';

const TaskControllerPage: React.FC = () => {
  const userId = localStorage.getItem('user_email');

  return (
    <div className="p-6 space-y-6">
      <TaskController userId={userId} />

    </div>
  );
};

export default TaskControllerPage;