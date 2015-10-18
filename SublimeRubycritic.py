import sublime, sublime_plugin, os, subprocess, webbrowser, threading

class SublimeRubycriticCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, "Hello, World!")


class NewCriticCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    #sublime.message_dialog(str(self.sublime_vars))
    self.sublime_vars = self.view.window().extract_variables()
    thread = GenerateCritic(self.sublime_vars)
    thread.start()
    sublime.status_message("[SublimeRubycritic] Processing new critic")



class GenerateCritic(threading.Thread):
    def __init__(self, dic):
      self.sublime_vars = dic
      self.folder = self.sublime_vars['folder']
      self.result = None
      threading.Thread.__init__(self)

    def run(self):
      os.chdir(self.folder)
      p = subprocess.Popen(['rubycritic', 'app', 'lib'], stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
      out, err = p.communicate()

      critic_url = "file://" + os.getcwd() + "/tmp/rubycritic/"
      if "file_path" in self.sublime_vars.keys():
        file_critic_path = self.sublime_vars['file_path'].replace(self.folder,'')[1:] + "/"
        file_name = self.sublime_vars['file_base_name']
        critic_url =  critic_url + file_critic_path + file_name + ".html"
      else:
        critic_url =  critic_url + "overview.html"

      webbrowser.open(critic_url)

      self.result = True
      return



