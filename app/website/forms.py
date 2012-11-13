# Copyright 2012 Madhusudan C.S. and whoever owns the copyright of this
# gist https://gist.github.com/1200165 because the code for the portions
# of this file is taken from that gist.
#
# This file models.py is part of my site madhusudancs.info.
#
# This program which runs madhusudancs.info is free software: you can
# redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from django import forms


class StringListField(forms.CharField):
    def prepare_value(self, value):
        return ', '.join(value)

    def to_python(self, value):
        if not value:
            return []
        return [item.strip() for item in value.split(',')]
