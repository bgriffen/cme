from Common import *


class ArrayAdapter(TabularAdapter):

    #columns = [('i', 'index'), ('p6', 0), ('p7', 1),  ('p8', 2),  ('p9', 3),  ('p10', 4)]
    columns = [ ('Name',    'name'),
                ('Age',     'age'),
                ('Address', 'address'),
                ('Spouse',  'spouse') ]

    #rows = [('i', 'index'),('nvir3', 0), ('nvir4', 1),  ('nvir5', 2),  ('nvir6', 3),  ('nvir7', 4),  ('nvir8', 5),  ('nvir9', 6)]

    # Font fails with wx in OSX; see traitsui issue #13:
    # font        = Font('Courier 10')
    alignment   = 'center'
    format      = '%.4f'
    index_text  = Str
    index_image = Str

    def _get_index_text(self):
        nvir3,nvir4,nvir5,nvir6,nvir7 = self.row
        return None
        #return str(self.item)

    def _get_index_image(self):
        p6,p7,p8,p9,p10 = self.item
        return '@icons:red_ball'
        return None

class Existence(HasTraits):

    data = Array
    data = np.random.random((10, 10))
    haloid = Enum(['190897','140666','208737'])
    halomasterdir = Directory

    view = View(Item(name='halomasterdir',springy=True,label='Directory'),
                Item(name='haloid',label='Cluster',padding=5),
                Item(name='data',show_label = False,style = 'readonly',editor = TabularEditor(adapter = ArrayAdapter()))
                )
                      
    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        self.halomasterdir = self.main.headertab.basepath
