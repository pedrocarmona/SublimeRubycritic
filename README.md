SublimeRubycritic
================================


## Installation

Before using this plugin, you must ensure that `rubycritic` is installed on your system. To install `rubycritic`, do the following:

1. Install [Ruby](http://www.ruby-lang.org). Sugestion: `rbenv`.

1. Install `rubycritic` by typing the following in a terminal:
   ```
   [sudo] gem install rubycritic
   ```

1. If you are using `rbenv`, ensure that they are loaded in your shell’s correct startup file.
  ```
  rbenv rehash
  ```
1. test in sublime console (View > show console)
  ```
  import os
  os.system("rubycritic")
  ```

1. If is result 0, then there is no need to do the next steps. 
 
1. If result is 32512, then sublime cannot find rubycritic. Please do these instructions in you command line:
  ```
  which rubycritic
  ```

1. copy the output and do this
  ```
  ln -s [OUTPUT] /usr/local/bin/rubycritic
  # rbenv example: ln -s /Users/YOURUSERNAME/.rbenv/shims/rubycritic /usr/local/bin/rubycritic
  ```

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

