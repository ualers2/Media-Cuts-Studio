
import { Check, X, AlertTriangle, HelpCircle } from 'lucide-react';

export const StatusLegend = () => {
  return (
    <div className="bg-white rounded-lg shadow-sm border p-4">
      <h3 className="font-semibold text-slate-800 mb-3 text-sm">Status Legend</h3>
      <div className="flex flex-wrap gap-4 text-sm">
        <div className="flex items-center space-x-2">
          <Check className="w-4 h-4 text-green-600" />
          <span className="text-slate-600">Service is operating normally</span>
        </div>
        <div className="flex items-center space-x-2">
          <AlertTriangle className="w-4 h-4 text-yellow-600" />
          <span className="text-slate-600">Service disruption</span>
        </div>
        <div className="flex items-center space-x-2">
          <X className="w-4 h-4 text-red-600" />
          <span className="text-slate-600">Service outage</span>
        </div>
        <div className="flex items-center space-x-2">
          <HelpCircle className="w-4 h-4 text-slate-400" />
          <span className="text-slate-600">No data available</span>
        </div>
      </div>
    </div>
  );
};
