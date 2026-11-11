const isGithubPages = process.env.GITHUB_PAGES === 'true';
const repoBasePath = isGithubPages ? '/whatsapp-employee-messenger' : '';

/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  trailingSlash: true,
  images: {
    unoptimized: true
  },
  basePath: repoBasePath,
  assetPrefix: repoBasePath || undefined,
  env: {
    NEXT_PUBLIC_BASE_PATH: repoBasePath
  }
};

export default nextConfig;
