// Include gulp
var gulp = require('gulp');

// Include Our Plugins
// For removing repeat files in tmp folder
var clean = require('gulp-clean');
var wait = require('gulp-wait');

// For default actions
var notify = require('gulp-notify');
var jade = require('gulp-jade');
var sasslint = require('gulp-scss-lint');
var sass = require('gulp-sass');
var coffeelint = require('gulp-coffeelint');
var coffee = require('gulp-coffee');
var sourcemaps = require('gulp-sourcemaps');

// For publishing
var minifyCSS = require('gulp-minify-css');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');

// Not implemented plugins
// var rename = require('gulp-rename');
// connect  = require('gulp-connect'),
// plumber  = require('gulp-plumber'),
// var imagemin = require('gulp-imagemin');
// var sourcemaps = require('gulp-sourcemaps');



//
//
// Order (To restore order)
//
//

// Clean out tmp folder to remove any compiled code
gulp.task('clean', function() {
  return gulp.src('tmp', {read: false})
    .pipe(clean())
    .pipe(wait(500));
});



//
//
// Default
//
//

// Jade conversion with index.jade moved into main folder
gulp.task('jade', function () {
  // Convert supporting Jade files
  gulp.src('src/**/*.jade', '!src/index.jade')
    .pipe(jade())
    .pipe(gulp.dest('tmp/'));

    // Convert index file for easy loading by Github Pages
  gulp.src('src/index.jade')
    .pipe(jade())
    .pipe(gulp.dest(''));
});

// Lint Sass for errors
gulp.task('sasslint', function () {
  gulp.src('src/styles/**/*.scss')
    .pipe(sasslint());
    // .pipe(sasslint.reporter());
});

// Compile SCSS files into ./styles, alert user of completion
gulp.task('sass', function () {
  gulp.src('src/styles/**/*.scss')
    .pipe(sass({
          noCache: true,
          style: "expanded",
          lineNumbers: true,
          loadPath: './assets/styles/*'
        }))
    .pipe(gulp.dest('tmp/styles'))
    .pipe(notify({
        message: "succSASS!"
      }));
});

// Lint coffee for errors
gulp.task('coffeelint', function () {
  gulp.src('src/scripts/**/*.coffee')
    .pipe(coffeelint())
    .pipe(coffeelint.reporter());
});

// Compile Coffee files into ./scripts
gulp.task('coffee', function () {
  gulp.src('src/scripts/**/*.coffee')
    // Writes sourcemaps inline in JS file
    .pipe(sourcemaps.init())
    .pipe(coffee())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('tmp/scripts'))
    .pipe(notify({
        message: "One more cup!"
      }));
});



//
//
// Publish Scripts
//
//

// Combine all CSS files into one for loading speed
gulp.task('minifyCSS', function () {
  gulp.src('tmp/styles/**/*.css')
    .pipe(clean({force: true}))
    .pipe(concat('styles.css'))
    .pipe(minifyCSS({keepBreaks:true}))
    .pipe(gulp.dest('tmp/styles/'));
});

// Uglify the JS for faster functions
gulp.task('uglify', function () {
  gulp.src('tmp/scripts/**/*.js')
    .pipe(clean({force: true}))
    .pipe(uglify())
    .pipe(concat("app.min.js"))
    .pipe(gulp.dest('tmp/scripts'));
});



//
//
// Group Tasks
//
//

gulp.task('default', ['jade', 'sasslint', 'sass', 'coffeelint', 'coffee']);
gulp.task('order', ['clean']);
gulp.task('publish', ['default', 'minifyCSS', 'uglify']);



//
//
// Always Watching
//
//

var watching = gulp.watch('gulpfile.js', ['default']);
watching.on('change', function(event) {
  console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
});

// Watch for changes in SCSS
var watcherSCSS = gulp.watch('src/styles/**/*.scss', ['sass']);
watcherSCSS.on('change', function(event) {
  console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
});

// Watch for changes in Coffee
var watcherCoffee = gulp.watch('src/scripts/**/*.coffee', ['coffeelint', 'coffee']);
watcherCoffee.on('change', function(event) {
  console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
});