/** @type {import('next').NextConfig} */
const nextConfig = {
    webpack: (config, { isServer }) => {
      // Add HTML loader only for client-side code
      if (!isServer) {
        config.module.rules.push({
          test: /\.html$/,
          loader: 'html-loader'
        });
      }
      return config;
    }
  };
  
export default nextConfig;
  