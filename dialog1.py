import gtk

class PyApp(gtk.Window):
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Dialog Demo")
      self.set_default_size(250, 200)
      fixed = gtk.Fixed()
      btn = gtk.Button("Show")
      btn.connect("clicked",self.show_sialog)
      fixed.put(btn,100,100)
      self.add(fixed)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
      
   def show_sialog(self, widget, data=None):
      dialog = gtk.Dialog("My dialog", \
         self, \
         gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, \
         (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT, \
         gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
      label = gtk.Label("Simple dialog")
      dialog.vbox.add(label)
      label.show()
      res = dialog.run()
      print res
      dialog.destroy()
if __name__ == '__main__':
   PyApp()
   gtk.main()
