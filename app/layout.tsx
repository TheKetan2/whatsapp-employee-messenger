import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = { title: 'Employee WhatsApp Messenger', description: 'Select employees and prepare WhatsApp messages.' , manifest: '/manifest.json', themeColor: '#075e54' };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }
