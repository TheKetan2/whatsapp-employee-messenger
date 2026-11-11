import type { Metadata, Viewport } from 'next';
import './globals.css';

const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? '';

export const metadata: Metadata = {
  title: 'WhatsApp Employee Messenger',
  applicationName: 'WA Messenger',
  description: 'Filter employees and auditors by District, Taluka, and Designation, and prepare WhatsApp messages.',
  manifest: `${basePath}/manifest.json`,
  appleWebApp: {
    capable: true,
    statusBarStyle: 'default',
    title: 'WA Messenger'
  },
  formatDetection: {
    telephone: false
  },
  icons: {
    icon: [
      { url: `${basePath}/icons/icon-192.png`, sizes: '192x192', type: 'image/png' },
      { url: `${basePath}/icons/icon-512.png`, sizes: '512x512', type: 'image/png' }
    ],
    apple: [{ url: `${basePath}/icons/apple-touch-icon.png`, sizes: '180x180', type: 'image/png' }]
  }
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  viewportFit: 'cover',
  themeColor: '#075e54'
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
