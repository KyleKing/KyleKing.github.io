Package.describe({
  name: 'kyleking:juxtapose-js',
  version: '0.0.1',
  // Brief, one-line summary of the package.
  summary: "KnightLab's JuxtaposeJS for Meteor",
  // URL to the Git repository containing the source code for this package.
  git: '',
  // By default, Meteor will default to using README.md for documentation.
  // To avoid submitting documentation, set this field to null.
  documentation: 'README.md'
});

Package.onUse(function(api) {
  api.versionsFrom('1.2.1');
  api.use('ecmascript');
  api.addFiles('juxtapose.js');
  api.addFiles('juxtapose.css');
});

// Package.onTest(function(api) {
//   api.use('ecmascript');
//   api.use('tinytest');
//   api.use('kyleking:juxtapose-js');
//   api.addFiles('juxtapose-js-tests.js');
// });
