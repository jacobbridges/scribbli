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
 * Compile sass files to one minified css file for "lander" app.
 */
gulp.task('lander:sass', function () {
  return gulp
    // Find all `.scss` files from the `lander/assets/stylesheets/` folder
    .src('./lander/assets/stylesheets/**/*.scss')
    // Initialize source maps
    .pipe(sourceMaps.init())
    // Run Sass on those files
    .pipe(sass(sassOptions).on('error', sass.logError))
    // Minify the compiled CSS into a single file
    .pipe(cleanCSS(cleanCssOptions, cleanCssCallback))
    // Write source maps
    .pipe(sourceMaps.write())
    // Write the resulting CSS in the output folder
    .pipe(gulp.dest('./lander/static/css'));
});
gulp.task('lander:watch', function() {
  return gulp
    // Watch all `.scss` files from the `lander/assets/stylesheets/` folder
    .watch('./lander/assets/stylesheets/**/*.scss', ['lander:sass'])
    // When there is a change, log a message in the console
    .on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
});

/***************************************************************************************************
 *  T Y P E S C R I P T
 **************************************************************************************************/

gulp.task("lander:ts", function () {
  // Change Typescript modules into brower commonjs modules
  return browserify({
    basedir: '.',
    debug: true,
    entries: ['./lander/assets/scripts/main.ts'],
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
    .pipe(gulp.dest("./lander/static/js"));
});

/***************************************************************************************************
 *  M A I N   T A S K S
 **************************************************************************************************/

gulp.task('lander', ['lander:sass', 'lander:ts']);