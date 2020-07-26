1.17.1 / 2014-01-22
==================

  * fix: expected messages in should.js (should.js#168)
  * fix: expect errno global in node versions < v0.9.11 (#1111)
  * fix: unreliable checkGlobals optimization (#1110)

1.17.0 / 2014-01-09
==================

  * add: able to require globals (describe, it, etc.) through mocha (#1077)
  * fix: abort previous run on --watch change (#1100)
  * fix: reset context for each --watch triggered run (#1099)
  * fix: error when cli can't resolve path or pattern (#799)
  * fix: canonicalize objects before stringifying and diffing them (#1079)
  * fix: make CR call behave like carriage return for non tty (#1087)


1.16.2 / 2013-12-23
==================

  * fix: couple issues with ie 8 (#1082, #1081)
  * fix: issue running the xunit reporter in browsers (#1068)
  * fix: issue with firefox < 3.5 (#725)


1.16.1 / 2013-12-19
==================

  * fix: recompiled for missed changes from the last release


1.16.0 / 2013-12-19
==================

  * add: Runnable.globals(arr) for per test global whitelist (#1046)
  * add: mocha.throwError(err) for assertion libs to call (#985)
  * remove: --watch's spinner (#806)
  * fix: duplicate test output for multi-line specs in spec reporter (#1006)
  * fix: gracefully exit on SIGINT (#1063)
  * fix expose the specified ui only in the browser (#984)
  * fix: ensure process exit code is preserved when using --no-exit (#1059)
  * fix: return true from window.onerror handler (#868)
  * fix: xunit reporter to use process.stdout.write (#1068)
  * fix: utils.clean(str) indentation (#761)
  * fix: xunit reporter returning test duration a NaN (#1039)

1.15.1 / 2013-12-03
==================

  * fix: recompiled for missed changes from the last release

1.15.0 / 2013-12-02
==================

  * add: `--no-exit` to prevent `process.exit()` (#1018)
  * fix: using inline diffs (#1044)
  * fix: show pending test details in xunit reporter (#1051)
  * fix: faster global leak detection (#1024)
  * fix: yui compression (#1035)
  * fix: wrapping long lines in test results (#1030, #1031)
  * fix: handle errors in hooks (#1043)

1.14.0 / 2013-11-02
==================

  * add: unified diff (#862)
  * add: set MOCHA_COLORS env var to use colors (#965)
  * add: able to override tests links in html reporters (#776)
  * remove: teamcity reporter (#954)
  * update: commander dependency to 2.0.0 (#1010)
  * fix: mocha --ui will try to require the ui if not built in, as --reporter does (#1022)
  * fix: send cursor commands only if isatty (#184, #1003)
  * fix: include assertion message in base reporter (#993, #991)
  * fix: consistent return of it, it.only, and describe, describe.only (#840)

1.13.0 / 2013-09-15
==================

  * add: sort test files with --sort (#813)
  * update: diff depedency to 1.0.7
  * update: glob dependency to 3.2.3 (#927)
  * fix: diffs show whitespace differences (#976)
  * fix: improve global leaks (#783)
  * fix: firefox window.getInterface leak
  * fix: accessing iframe via window[iframeIndex] leak
  * fix: faster global leak checking
  * fix: reporter pending css selector (#970)

1.12.1 / 2013-08-29
==================

 * remove test.js from .gitignore
 * update included version of ms.js

1.12.0 / 2013-07-01
==================

 * add: prevent diffs for differing types. Closes #900
 * add `Mocha.process` hack for phantomjs
 * fix: use compilers with requires
 * fix regexps in diffs. Closes #890
 * fix xunit NaN on failure. Closes #894
 * fix: strip tab indentation in `clean` utility method
 * fix: textmate bundle installation

1.11.0 / 2013-06-12
==================

 * add --prof support
 * add --harmony support
 * add --harmony-generators support
 * add "Uncaught " prefix to uncaught exceptions
 * add web workers support
 * add `suite.skip()`
 * change to output # of pending / passing even on failures. Closes #872
 * fix: prevent hooks from being called if we are bailing
 * fix `this.timeout(0)`

1.10.0 / 2013-05-21
==================

 * add add better globbing support for windows via `glob` module
 * add support to pass through flags such as --debug-brk=1234. Closes #852
 * add test.only, test.skip to qunit interface
 * change to always use word-based diffs for now. Closes #733
 * change `mocha init` tests.html to index.html
 * fix `process` global leak in the browser
 * fix: use resolve() instead of join() for --require
 * fix: filterLeaks() condition to not consider indices in global object as leaks
 * fix: restrict mocha.css styling to #mocha id
 * fix: save timer references to avoid Sinon interfering in the browser build.

1.9.0 / 2013-04-03
==================

  * add improved setImmediate implementation
  * replace --ignore-leaks with --check-leaks
  * change default of ignoreLeaks to true. Closes #791
  * remove scrolling for HTML reporter
  * fix retina support
  * fix tmbundle, restrict to js scope

1.8.2 / 2013-03-11
==================

  * add `setImmediate` support for 0.10.x
  * fix mocha -w spinner on windows

1.8.1 / 2013-01-09
==================

  * fix .bail() arity check causing it to default to true

1.8.0 / 2013-01-08
==================

  * add Mocha() options bail support
  * add `Mocha#bail()` method
  * add instanceof check back for inheriting from Error
  * add component.json
  * add diff.js to browser build
  * update growl
  * fix TAP reporter failures comment :D

1.7.4 / 2012-12-06
==================

  * add total number of passes and failures to TAP
  * remove .bind() calls. re #680
  * fix indexOf. Closes #680

1.7.3 / 2012-11-30
==================

  * fix uncaught error support for the browser
  * revert uncaught "fix" which breaks node

1.7.2 / 2012-11-28
==================

  * fix uncaught errors to expose the original error message

1.7.0 / 2012-11-07
==================

  * add `--async-only` support to prevent false positives for missing `done()`
  * add sorting by filename in code coverage
  * add HTML 5 doctype to browser template.
  * add play button to html reporter to rerun a single test
  * add `this.timeout(ms)` as Suite#timeout(ms). Closes #599
  * update growl dependency to 1.6.x
  * fix encoding of test-case ?grep. Closes #637
  * fix unicode chars on windows
  * fix dom globals in Opera/IE. Closes #243
  * fix markdown reporter a tags
  * fix `this.timeout("5s")` support

1.6.0 / 2012-10-02
==================

  * add object diffs when `err.showDiff` is present
  * add hiding of empty suites when pass/failures are toggled
  * add faster `.length` checks to `checkGlobals()` before performing the filter

1.5.0 / 2012-09-21
==================

  * add `ms()` to `.slow()` and `.timeout()`
  * add `Mocha#checkLeaks()` to re-enable global leak checks
  * add `this.slow()` option [aheckmann]
  * add tab, CR, LF to error diffs for now
  * add faster `.checkGlobals()` solution [guille]
  * remove `fn.call()` from reduce util
  * remove `fn.call()` from filter util
  * fix forEach. Closes #582
  * fix relaying of signals [TooTallNate]
  * fix TAP reporter grep number

1.4.2 / 2012-09-01
==================

  * add support to multiple `Mocha#globals()` calls, and strings
  * add `mocha.reporter()` constructor support [jfirebaugh]
  * add `mocha.timeout()`
  * move query-string parser to utils.js
  * move highlight code to utils.js
  * fix third-party reporter support [exogen]
  * fix client-side API to match node-side [jfirebaugh]
  * fix mocha in iframe [joliss]

1.4.1 / 2012-08-28
==================

  * add missing `Markdown` export
  * fix `Mocha#grep()`, escape regexp strings
  * fix reference error when `devicePixelRatio` is not defined. Closes #549

1.4.0 / 2012-08-22
==================

  * add mkdir -p to `mocha init`. Closes #539
  * add `.only()`. Closes #524
  * add `.skip()`. Closes #524
  * change str.trim() to use utils.trim(). Closes #533
  * fix HTML progress indicator retina display
  * fix url-encoding of click-to-grep HTML functionality

1.3.2 / 2012-08-01
==================

  * fix exports double-execution regression. Closes #531

1.3.1 / 2012-08-01
==================

  * add passes/failures toggling to HTML reporter
  * add pending state to `xit()` and `xdescribe()` [Brian Moore]
  * add th                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Added support for `window.onerror` [guillermo]
  * Fixed: clear timeout on uncaught exceptions. Closes #131 [guillermo]
  * Added `mocha.css` to PHONY list.
  * Added `mocha.js` to PHONY list.

0.3.4 / 2011-12-08
==================

  * Added: allow `done()` to be called with non-Error
  * Added: return Runner from `mocha.run()`. Closes #126
  * Fixed: run afterEach even on failures. Closes #125
  * Fixed clobbering of current runnable. Closes #121

0.3.3 / 2011-12-08
==================

  * Fixed hook timeouts. Closes #120
  * Fixed uncaught exceptions in hooks

0.3.2 / 2011-12-05
==================

  * Fixed weird reporting when `err.message` is not present

0.3.1 / 2011-12-04
==================

  * Fixed hook event emitter leak. Closes #117
  * Fixed: export `Spec` constructor. Closes #116

0.3.0 / 2011-12-04
==================

  * Added `-w, --watch`. Closes #72
  * Added `--ignore-leaks` to ignore global leak checking
  * Added browser `?grep=pattern` support
  * Added `--globals <names>` to specify accepted globals. Closes #99
  * Fixed `mocha-debug(1)` on some systems. Closes #232
  * Fixed growl total, use `runner.total`

0.2.0 / 2011-11-30
==================

  * Added `--globals <names>` to specify accepted globals. Closes #99
  * Fixed funky highlighting of messages. Closes #97
  * Fixed `mocha-debug(1)`. Closes #232
  * Fixed growl total, use runner.total

0.1.0 / 2011-11-29
==================

  * Added `suiteSetup` and `suiteTeardown` to TDD interface [David Henderson]
  * Added growl icons. Closes #84
  * Fixed coffee-script support

0.0.8 / 2011-11-25
==================

  * Fixed: use `Runner#total` for accurate reporting

0.0.7 / 2011-11-25
==================

  * Added `Hook`
  * Added `Runnable`
  * Changed: `Test` is `Runnable`
  * Fixed global leak reporting in hooks
  * Fixed: > 2 calls to done() only report the error once
  * Fixed: clear timer on failure. Closes #80

0.0.6 / 2011-11-25
==================

  * Fixed return on immediate async error. Closes #80

0.0.5 / 2011-11-24
==================

  * Fixed: make mocha.opts whitespace less picky [kkaefer]

0.0.4 / 2011-11-24
==================

  * Added `--interfaces`
  * Added `--reporters`
  * Added `-c, --colors`. Closes #69
  * Fixed hook timeouts

0.0.3 / 2011-11-23
==================

  * Added `-C, --no-colors` to explicitly disable
  * Added coffee-script support

0.0.2 / 2011-11-22
==================

  * Fixed global leak detection due to Safari bind() change
  * Fixed: escape html entities in Doc reporter
  * Fixed: escape html entities in HTML reporter
  * Fixed pending test support for HTML reporter. Closes #66

0.0.1 / 2011-11-22
==================

  * Added `--timeout` second shorthand support, ex `--timeout 3s`.
  * Fixed "test end" event for uncaughtExceptions. Closes #61

0.0.1-alpha6 / 2011-11-19
==================

  * Added travis CI support (needs enabling when public)
  * Added preliminary browser support
  * Added `make mocha.css` target. Closes #45
  * Added stack trace to TAP errors. Closes #52
  * Renamed tearDown to teardown. Closes #49
  * Fixed: cascading hooksc. Closes #30
  * Fixed some colors for non-tty
  * Fixed errors thrown in sync test-cases due to nextTick
  * Fixed Base.window.width... again give precedence to 0.6.x

0.0.1-alpha5 / 2011-11-17
==================

  * Added `doc` reporter. Closes #33
  * Added suite merging. Closes #28
  * Added TextMate bundle and `make tm`. Closes #20

0.0.1-alpha4 / 2011-11-15
==================

  * Fixed getWindowSize() for 0.4.x

0.0.1-alpha3 / 2011-11-15
==================

  * Added `-s, --slow <ms>` to specify "slow" test threshold
  * Added `mocha-debug(1)`
  * Added `mocha.opts` support. Closes #31
  * Added: default [files] to _test/*.js_
  * Added protection against multiple calls to `done()`. Closes #35
  * Changed: bright yellow for slow Dot reporter tests

0.0.1-alpha1 / 2011-11-08
==================

  * Missed this one :)

0.0.1-alpha1 / 2011-11-08
==================

  * Initial release
