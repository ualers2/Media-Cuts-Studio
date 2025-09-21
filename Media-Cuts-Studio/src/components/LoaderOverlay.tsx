// components/LoaderOverlay.tsx
import { Loader2 } from "lucide-react"

export default function LoaderOverlay({ message }: { message: string }) {
  return (
    <div className="fixed inset-0 bg-black/50 z-50 flex flex-col items-center justify-center">
      <Loader2 className="h-12 w-12 animate-spin text-white mb-4" />
      <p className="text-white text-lg font-semibold">{message}</p>
    </div>
  )
}
