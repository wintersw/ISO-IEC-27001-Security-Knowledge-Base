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
          exclude: ['includes/**'],
          numberPrefixParser: false,
          editUrl:
            'https://github.com/wintersw/ISO-IEC-27001-Security-Knowledge-Base/tree/main/',
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,
        },
        blog: false,
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
