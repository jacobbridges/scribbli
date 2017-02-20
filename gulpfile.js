// Import gulp stuff
var gulp = require('gulp');
var gutil = require('gulp-util');
var sourceMaps = require('gulp-sourcemaps');

// Import sass stuff
var sass = require('gulp-sass');
var cleanCSS = require('gulp-clean-css');

// Import typescript stuff
var browserify = require("browserify");
var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');
var tsify = require("tsify");
var uglify = require('gulp-uglify');


/***************************************************************************************************
 *  S A S S
 **************************************************************************************************/

var sassOptions = {
  errLogToConsole: true,
  outputStyle: 'expanded'
};

var cleanCssOptions = {
  debug: true,
  compatibility: 'ie8'
};

var cleanCssCallback = function(details) {
  var originalKb = Math.round((details.stats.originalSize / 1024.0)*10)/10;
  var minifiedKb = Math.round((details.stats.minifiedSize / 1024.0)*10)/10;
  gutil.log('Minified ' + details.name + ': ' + originalKb + 'kb -> ' + minifiedKb + 'kb');
};

/**
 * Create a generic pipeline for compiling all scss files into one css file.
 */

var scssGulpPipeline = function(gulp_, source, destination) {
  return gulp_
    // Find all `.scss` files from the `lander/assets/stylesheets/` folder
    .src(source)
    // Initialize source maps
    .pipe(sourceMaps.init())
    // Run Sass on those files
    .pipe(sass(sassOptions).on('error', sass.logError))
    // Minify the compiled CSS into a single file
    .pipe(cleanCSS(cleanCssOptions, cleanCssCallback))
    // Write source maps
    .pipe(sourceMaps.write())
    // Write the resulting CSS in the output folder
    .pipe(gulp.dest(destination));
};


/***************************************************************************************************
 *  T Y P E S C R I P T
 **************************************************************************************************/

/**
 * Create a generic pipeline for compiling all TypeScript files into one minified JS file.
 */
var tsGulpPipeline = function(gulp_, browserify_, entryPoints, destinationPath) {
  // Change Typescript modules into brower commonjs modules
  return browserify({
    basedir: '.',
    debug: true,
    entries: entryPoints,
    cache: {},
    packageCache: {}
  })
    .plugin(tsify)
    .bundle()
    .pipe(source('mini.js'))
    .pipe(buffer())
    .pipe(sourceMaps.init({loadMaps: true}))
    .pipe(uglify())
    .pipe(sourceMaps.write('./'))
    .pipe(gulp.dest(destinationPath));
};


/***************************************************************************************************
 * L A N D E R   T A S K S
 **************************************************************************************************/

gulp.task('lander:sass', function () {
  return scssGulpPipeline(gulp, './lander/assets/stylesheets/**/*.scss', './lander/static/lander/css');
});
gulp.task('lander:ts', function () {
  return tsGulpPipeline(gulp, browserify, ['./lander/assets/scripts/main.ts'], './lander/static/lander/js');
});
gulp.task('lander:sass:watch', function () {
  return gulp
    // Watch all `.scss` files from the `lander/assets/stylesheets/` folder
    .watch('./lander/assets/stylesheets/**/*.scss', ['lander:sass'])
    // When there is a change, log a message in the console
    .on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
});
gulp.task('lander:ts:watch', function () {
  return gulp
    // Watch all `.ts` files from the `lander/assets/scripts` folder
    .watch('./lander/assets/scripts/**/*.ts', ['lander:ts'])
    // When there is a change, log a message in the console
    .on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
});


/***************************************************************************************************
 * A L P H A   T A S K S
 **************************************************************************************************/

gulp.task('alpha:sass', function () {
  return scssGulpPipeline(gulp, './alpha/assets/stylesheets/**/*.scss', './alpha/static/alpha/css');
});
gulp.task('alpha:ts', function () {
  return tsGulpPipeline(gulp, browserify, ['./alpha/assets/scripts/main.ts'], './alpha/static/alpha/js');
});
gulp.task('alpha:sass:watch', function () {
  return gulp
    // Watch all `.scss` files from the `alpha/assets/stylesheets/` folder
    .watch('./alpha/assets/stylesheets/**/*.scss', ['alpha:sass'])
    // When there is a change, log a message in the console
    .on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
});
gulp.task('alpha:ts:watch', function () {
  return gulp
    // Watch all `.ts` files from the `alpha/assets/scripts` folder
    .watch('./alpha/assets/scripts/**/*.ts', ['alpha:ts'])
    // When there is a change, log a message in the console
    .on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
});


/***************************************************************************************************
 *  M A I N   T A S K S
 **************************************************************************************************/

gulp.task('lander', ['lander:sass', 'lander:ts']);
gulp.task('lander:watch', ['lander:sass:watch', 'lander:ts:watch']);
gulp.task('alpha', ['alpha:sass', 'alpha:ts']);
gulp.task('alpha:watch', ['alpha:sass:watch', 'alpha:ts:watch']);