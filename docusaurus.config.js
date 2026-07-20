// @ts-check

const {themes} = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'ISO/IEC 27001 Security Knowledge Base',
  tagline: 'Practical security documentation for ISMS teams',
  url: 'https://wintersw.github.io',
  baseUrl: '/ISO-IEC-27001-Security-Knowledge-Base/',
  organizationName: 'wintersw',
  projectName: 'ISO-IEC-27001-Security-Knowledge-Base',
  deploymentBranch: 'gh-pages',
  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',
  onDuplicateRoutes: 'warn',
  trailingSlash: false,
  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'throw',
    },
  },
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          numberPrefixParser: false,
          editUrl:
            'https://github.com/wintersw/ISO-IEC-27001-Security-Knowledge-Base/tree/main/',
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,
        },
        blog: false,
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
          ignorePatterns: ['/tags/**'],
          filename: 'sitemap.xml',
        },
      }),
    ],
  ],
  themes: [
    '@docusaurus/theme-mermaid',
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        indexDocs: true,
        indexPages: true,
        indexBlog: false,
        docsRouteBasePath: '/',
        highlightSearchTermsOnTargetPage: true,
        explicitSearchResultPath: true,
        searchResultLimits: 15,
      },
    ],
  ],
  themeConfig: {
    metadata: [
      {
        name: 'keywords',
        content:
          'ISO 27001, ISO/IEC 27001, ISMS, information security, cybersecurity, risk management, Annex A',
      },
      {name: 'robots', content: 'index,follow,max-image-preview:large'},
    ],
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'ISO 27001 KB',
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'left',
          label: 'Documentation',
        },
        {to: '/00-getting-started/learning-paths', label: 'Learning paths', position: 'left'},
        {to: '/06-annex-a/', label: 'Annex A', position: 'left'},
        {to: '/10-templates/', label: 'Templates', position: 'left'},
        {to: '/17-mappings/', label: 'Mappings', position: 'left'},
        {
          href: 'https://github.com/wintersw/ISO-IEC-27001-Security-Knowledge-Base',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} ISO/IEC 27001 Security Knowledge Base.`,
    },
    prism: {
      theme: themes.github,
      darkTheme: themes.dracula,
    },
    tableOfContents: {
      minHeadingLevel: 2,
      maxHeadingLevel: 4,
    },
  },
};

module.exports = config;
