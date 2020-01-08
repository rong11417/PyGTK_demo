import gtk

class PyApp(gtk.Window):
  def __init__(self):
    super(PyApp,self).__init__()

    self.set_title("Alignment demo")
    self.set_size_request(400,200)
    self.set_position(gtk.WIN_POS_CENTER)
  
    vbox=gtk.VBox(False,5)
    vb=gtk.VBox()
    hbox=gtk.HBox(True,3)
    valign=gtk.Alignment(0.5,0.25,0,0)
    lbl = gtk.Label("you name?")
    vb.pack_start(lbl, True, True, 10)
    text = gtk.Entry()
    vb.pack_start(text, True, True, 10)
    valign.add(vb)
    vbox.pack_start(valign)
		
    ok = gtk.Button("OK")
    ok.set_size_request(70, 30)
		
    close = gtk.Button("Close")
    hbox.add(ok)
    hbox.add(close)
		
    halign = gtk.Alignment(1, 0, 0, 0)
    halign.add(hbox)
		
    vbox.pack_start(halign, False, False, 3)
		
    self.add(vbox)
    self.connect("destroy", gtk.main_quit)
    self.show_all()
PyApp()
gtk.main()
