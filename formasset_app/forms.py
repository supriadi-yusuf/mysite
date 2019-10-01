from django import forms

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all' : ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')

class OtherWidget(forms.TextInput):
    class Media:
        js = ('whizbang.js',)

class StudentForm(forms.Form):
    name = forms.CharField()
    birth_date = forms.DateField(widget=CalendarWidget)

class StudentForm2(forms.Form):
    name = forms.CharField()
    birth_date = forms.DateField(widget=CalendarWidget)

    class Media:
        css = {
            'all' : ('layout.css',)
        }

class FancyCalendarWidget(CalendarWidget):
    class Media:
        css = {
            'all' : ('fancy.css',)
        }

        js = ('whizbang.js',)

class FancyCalendarWidget2(CalendarWidget):
    class Media:
        extend = False

        css = {
            'all' : ('fancy.css',)
        }

        js = ('whizbang.js',)

class CalendarWidget2(forms.TextInput):
    @property
    def media(self):
        return forms.Media(
            css = {
                'all' : ('pretty.css',)
            },
            js = ('animations.js','actions.js')
        )

class CalendarWidget3(forms.TextInput):
    class Media:
        css = {
            'all' : ('/css/pretty.css',) # absolute
        }
        js = ( 'animations.js', #relative
               'http://othersite.com/actions.js') # absolute
