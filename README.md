# Employee WhatsApp Messenger

A local-first Next.js app for selecting employees from an Excel directory and preparing individual WhatsApp messages.

## Included directory

`public/employees.json` contains 48 non-vacant rows with valid 10-digit phone numbers extracted from the first employee table in the supplied workbook. The second table was not imported because it does not contain mobile numbers.

## Run locally

Requirements: Node.js 18.17+.

```bash
npm install
npm run dev
```

Open http://localhost:3000.

## Build

```bash
npm run build
npm start
```

## Deployment

Deploy as a standard Next.js app on Vercel or another Node.js host. The app does not require a database or API server for its current features. Employee data is saved in browser localStorage. If hosted publicly, do not put sensitive or non-public employee data in the public JSON file; replace the bundled directory with a private, user-provided import or add authentication and server-side access controls.

## WhatsApp behavior and limitations

- Text-only: opens `https://wa.me/91<number>` with the message prefilled. The user presses Send in WhatsApp.
- Image + text: uses the browser Web Share API when supported. The user must choose WhatsApp and then the intended chat. The app cannot programmatically preselect a WhatsApp recipient or guarantee that WhatsApp is available in the share sheet.
- For unsupported browsers, open the WhatsApp chat and attach the image manually.
- No messages are sent automatically. This is deliberate: WhatsApp does not offer a supported multi-recipient click-to-chat URL for this workflow.

## Excel import

The first worksheet is read in-browser. Expected columns: serial number, designation, employee name, class/grade, mobile number. It imports non-vacant rows with valid 10-digit Indian mobile numbers. Data stays in the current browser's localStorage.
