import React from 'react';

export const Popover = ({ children, isOpen, close }) => {
  return (
    isOpen && (
      <div className="absolute bg-white shadow-lg rounded p-4">
        {children}
        <button onClick={close} className="text-right text-red-500">Close</button>
      </div>
    )
  );
};

export const PopoverTrigger = ({ children, onClick }) => {
  return (
    <button onClick={onClick} className="text-blue-500">
      {children}
    </button>
  );
};

export const PopoverContent = ({ children }) => {
  return <div>{children}</div>;
};
