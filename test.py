
import gtk
class PyApp(gtk.Window):
  def __init__(self):
    super(PyApp,self).__init__()
    #self.set_title("Hello World")
    #self.set_default_size(400,300)
    #self.set_position(gtk.WIN_POS_CENTER)
    self.show_all()
  def on_abtdlg(self, widget):
   
    about = gtk.AboutDialog()
    about.set_program_name("PyGTK Dialog")
    about.set_version("0.1")
    about.set_authors("M.V.Lathkar")
    about.set_copyright("(c) TutorialsPoint")
    about.set_comments("About Dialog example")
    about.set_website("http://www.tutorialspoint.com")
   
    about.run()
    about.destroy()
PyApp()
gtk.main()
