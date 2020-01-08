import gtk

class PyApp(gtk.Window):
   
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("layout")
      self.set_size_request(300,200)
      self.set_position(gtk.WIN_POS_CENTER)
      sc = gtk.ScrolledWindow()
      lo = gtk.Layout()
      lo.set_size(400,400)
      button = gtk.Button("Press Me")
      lo.put(button, 125,200)
      sc.add(lo)
      self.add(sc)
      self.connect("destroy", gtk.main_quit)
      self.show_all()

PyApp()
gtk.main()
