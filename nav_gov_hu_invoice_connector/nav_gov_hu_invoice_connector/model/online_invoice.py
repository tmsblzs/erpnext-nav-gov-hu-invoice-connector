#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Mon Jun  6 15:33:22 2022 by generateDS.py version 2.39.2.
# Python 3.7.3 (default, Jan 22 2021, 20:04:44)  [GCC 8.3.0]
#
# Command line options:
#   ('-o', 'online_invoice.py')
#   ('-c', 'catalog.xml')
#   ('-s', 'invoice_subclass')
#   ('--external-encoding', 'utf-8')
#   ('--export', 'write etree literal')
#   ('--output-directory', 'generatedDS')
#
# Command line arguments:
#   onlineInvoice.xsd
#
# Command line:
#   /home/frappe/.local/bin/generateDS -o "online_invoice.py" -c "catalog.xml" -s "invoice_subclass" --external-encoding="utf-8" --export="write etree literal" --output-directory="generatedDS" onlineInvoice.xsd
#
# Current working directory (os.getcwd()):
#   v3
#
import datetime
import sys

import pytz

try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            # if input_data.microsecond == 0:
            #     _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
            #         input_data.year,
            #         input_data.month,
            #         input_data.day,
            #         input_data.hour,
            #         input_data.minute,
            #         input_data.second,
            #     )
            # else:
            #     _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
            #         input_data.year,
            #         input_data.month,
            #         input_data.day,
            #         input_data.hour,
            #         input_data.minute,
            #         input_data.second,
            #         ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            #     )
            # if input_data.tzinfo is not None:
            #     tzoff = input_data.tzinfo.utcoffset(input_data)
            #     if tzoff is not None:
            #         total_seconds = tzoff.seconds + (86400 * tzoff.days)
            #         if total_seconds == 0:
            #             _svalue += 'Z'
            #         else:
            #             if total_seconds < 0:
            #                 _svalue += '-'
            #                 total_seconds *= -1
            #             else:
            #                 _svalue += '+'
            #             hours = total_seconds // 3600
            #             minutes = (total_seconds - (hours * 3600)) // 60
            #             _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            # return _svalue
            return input_data.isoformat()[:-3] + "Z"
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'utf-8'
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#



















# end class InvoiceChainQueryType


# end class InvoiceDataResultType


# end class InvoiceDigestResultType


# end class InvoiceDigestType


# end class InvoiceLinesType


# end class InvoiceNumberQueryType


# end class InvoiceOperationListType


# end class InvoiceOperationType


# end class InvoiceQueryParamsType


# end class InvoiceReferenceDataType


# end class ManageAnnulmentRequestType


# end class ManageInvoiceRequestType


# end class MandatoryQueryParamsType


# end class NewCreatedLinesType


# end class PointerType


# end class ProcessingResultListType


# end class ProcessingResultType


# end class QueryInvoiceChainDigestRequestType


# end class QueryInvoiceChainDigestResponseType


# end class QueryInvoiceCheckResponseType


# end class QueryInvoiceDataRequestType


# end class QueryInvoiceDataResponseType


# end class QueryInvoiceDigestRequestType


# end class QueryInvoiceDigestResponseType


# end class QueryTaxpayerRequestType


# end class QueryTaxpayerResponseType


# end class QueryTransactionListRequestType


# end class QueryTransactionListResponseType


# end class QueryTransactionStatusRequestType


# end class QueryTransactionStatusResponseType


# end class RelationalQueryParamsType


# end class RelationQueryDateType


# end class RelationQueryMonetaryType


# end class SoftwareType


# end class TaxpayerAddressItemType


# end class TaxpayerAddressListType


# end class TaxpayerDataType


# end class TokenExchangeResponseType


# end class TransactionListResultType


# end class TransactionQueryParamsType


# end class TransactionResponseType


# end class TransactionType


# end class GeneralErrorResponse


# end class ManageAnnulmentRequest


# end class ManageAnnulmentResponse


# end class ManageInvoiceRequest


# end class ManageInvoiceResponse


# end class QueryInvoiceChainDigestRequest


# end class QueryInvoiceChainDigestResponse


# end class QueryInvoiceCheckRequest


# end class QueryInvoiceCheckResponse


# end class QueryInvoiceDataRequest


# end class QueryInvoiceDataResponse


# end class QueryInvoiceDigestRequest


# end class QueryInvoiceDigestResponse


# end class QueryTaxpayerRequest


# end class QueryTaxpayerResponse


# end class QueryTransactionListRequest


# end class QueryTransactionListResponse


# end class QueryTransactionStatusRequest


# end class QueryTransactionStatusResponse


# end class TokenExchangeRequest


# end class TokenExchangeResponse


# end class AdditionalDataType


# end class AdvanceDataType


# end class AdvancePaymentDataType


# end class AggregateInvoiceLineDataType


# end class AircraftType


# end class BatchInvoiceType


# end class ContractNumbersType


# end class ConventionalInvoiceInfoType


# end class CostCentersType


# end class CustomerCompanyCodesType


# end class CustomerDeclarationType


# end class CustomerInfoType


# end class CustomerTaxNumberType


# end class CustomerVatDataType


class DealerCodesType(GeneratedsSuper):
    """DealerCodesType -- Besz
    á
    ll
    í
    t
    ó
    k
    ó
    dok
    Dealer codes
    dealerCode -- Besz
    á
    ll
    í
    t
    ó
    k
    ó
    d
    Dealer code

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, dealerCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if dealerCode is None:
            self.dealerCode = []
        else:
            self.dealerCode = dealerCode
        self.dealerCode_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DealerCodesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DealerCodesType.subclass:
            return DealerCodesType.subclass(*args_, **kwargs_)
        else:
            return DealerCodesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_dealerCode(self):
        return self.dealerCode
    def set_dealerCode(self, dealerCode):
        self.dealerCode = dealerCode
    def add_dealerCode(self, value):
        self.dealerCode.append(value)
    def insert_dealerCode_at(self, index, value):
        self.dealerCode.insert(index, value)
    def replace_dealerCode_at(self, index, value):
        self.dealerCode[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.dealerCode
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='DealerCodesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DealerCodesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DealerCodesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DealerCodesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DealerCodesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DealerCodesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='DealerCodesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for dealerCode_ in self.dealerCode:
            namespaceprefix_ = self.dealerCode_nsprefix_ + ':' if (UseCapturedNS_ and self.dealerCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdealerCode>%s</%sdealerCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(dealerCode_), input_name='dealerCode')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='DealerCodesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for dealerCode_ in self.dealerCode:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}dealerCode').text = self.gds_format_string(dealerCode_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DealerCodesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('dealerCode=[\n')
        level += 1
        for dealerCode_ in self.dealerCode:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(dealerCode_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'dealerCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dealerCode')
            value_ = self.gds_validate_string(value_, node, 'dealerCode')
            self.dealerCode.append(value_)
            self.dealerCode_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.dealerCode[-1])
# end class DealerCodesType


class DeliveryNotesType(GeneratedsSuper):
    """DeliveryNotesType -- Sz
    á
    ll
    í
    t
    ó
    lev
    é
    l sz
    á
    mok
    Delivery notes
    deliveryNote -- Sz
    á
    ll
    í
    t
    ó
    lev
    é
    l sz
    á
    m
    Delivery note

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, deliveryNote=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if deliveryNote is None:
            self.deliveryNote = []
        else:
            self.deliveryNote = deliveryNote
        self.deliveryNote_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DeliveryNotesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DeliveryNotesType.subclass:
            return DeliveryNotesType.subclass(*args_, **kwargs_)
        else:
            return DeliveryNotesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_deliveryNote(self):
        return self.deliveryNote
    def set_deliveryNote(self, deliveryNote):
        self.deliveryNote = deliveryNote
    def add_deliveryNote(self, value):
        self.deliveryNote.append(value)
    def insert_deliveryNote_at(self, index, value):
        self.deliveryNote.insert(index, value)
    def replace_deliveryNote_at(self, index, value):
        self.deliveryNote[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.deliveryNote
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='DeliveryNotesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DeliveryNotesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DeliveryNotesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DeliveryNotesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DeliveryNotesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DeliveryNotesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='DeliveryNotesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for deliveryNote_ in self.deliveryNote:
            namespaceprefix_ = self.deliveryNote_nsprefix_ + ':' if (UseCapturedNS_ and self.deliveryNote_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdeliveryNote>%s</%sdeliveryNote>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(deliveryNote_), input_name='deliveryNote')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='DeliveryNotesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for deliveryNote_ in self.deliveryNote:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}deliveryNote').text = self.gds_format_string(deliveryNote_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DeliveryNotesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('deliveryNote=[\n')
        level += 1
        for deliveryNote_ in self.deliveryNote:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(deliveryNote_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'deliveryNote':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'deliveryNote')
            value_ = self.gds_validate_string(value_, node, 'deliveryNote')
            self.deliveryNote.append(value_)
            self.deliveryNote_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.deliveryNote[-1])
# end class DeliveryNotesType


class DetailedReasonType(GeneratedsSuper):
    """DetailedReasonType -- Mentess
    é
    g, kiv
    é
    tel r
    é
    szletes indokol
    á
    sa
    Detailed justification of exemption
    case -- Az eset le
    í
    r
    á
    sa k
    ó
    ddal
    Case notation with code
    reason -- Az eset le
    í
    r
    á
    sa sz
    ö
    veggel
    Case notation with text

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, case=None, reason=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.case = case
        self.validate_SimpleText50NotBlankType(self.case)
        self.case_nsprefix_ = "common"
        self.reason = reason
        self.validate_SimpleText200NotBlankType(self.reason)
        self.reason_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DetailedReasonType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DetailedReasonType.subclass:
            return DetailedReasonType.subclass(*args_, **kwargs_)
        else:
            return DetailedReasonType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_case(self):
        return self.case
    def set_case(self, case):
        self.case = case
    def get_reason(self):
        return self.reason
    def set_reason(self, reason):
        self.reason = reason
    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_SimpleText200NotBlankType(self, value):
        result = True
        # Validate type SimpleText200NotBlankType, a restriction on AtomicStringType200.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 200:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText200NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText200NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText200NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText200NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText200NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.case is not None or
            self.reason is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='DetailedReasonType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DetailedReasonType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DetailedReasonType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DetailedReasonType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DetailedReasonType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DetailedReasonType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='DetailedReasonType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.case is not None:
            namespaceprefix_ = self.case_nsprefix_ + ':' if (UseCapturedNS_ and self.case_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scase>%s</%scase>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.case), input_name='case')), namespaceprefix_ , eol_))
        if self.reason is not None:
            namespaceprefix_ = self.reason_nsprefix_ + ':' if (UseCapturedNS_ and self.reason_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreason>%s</%sreason>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.reason), input_name='reason')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='DetailedReasonType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.case is not None:
            case_ = self.case
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}case').text = self.gds_format_string(case_)
        if self.reason is not None:
            reason_ = self.reason
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}reason').text = self.gds_format_string(reason_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DetailedReasonType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.case is not None:
            showIndent(outfile, level)
            outfile.write('case=%s,\n' % self.gds_encode(quote_python(self.case)))
        if self.reason is not None:
            showIndent(outfile, level)
            outfile.write('reason=%s,\n' % self.gds_encode(quote_python(self.reason)))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'case':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'case')
            value_ = self.gds_validate_string(value_, node, 'case')
            self.case = value_
            self.case_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.case)
        elif nodeName_ == 'reason':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'reason')
            value_ = self.gds_validate_string(value_, node, 'reason')
            self.reason = value_
            self.reason_nsprefix_ = child_.prefix
            # validate type SimpleText200NotBlankType
            self.validate_SimpleText200NotBlankType(self.reason)
# end class DetailedReasonType


class DieselOilPurchaseType(GeneratedsSuper):
    """DieselOilPurchaseType -- G
    á
    zolaj ad
    ó
    zottan t
    ö
    rt
    é
    n
    ő
    beszerz
    é
    s
    é
    nek adatai
    –
    45/2016 (XI. 29.) NGM rendelet 75.
    §
    (1) a)
    Data of gas oil acquisition after taxation
    –
    point a), paragraph (1) of Section 75 of the NGM Decree No. 45/2016. (XI. 29.)
    purchaseLocation -- G
    á
    zolaj beszerz
    é
    s helye
    Place of purchase of the gas oil
    purchaseDate -- G
    á
    zolaj beszerz
    é
    s d
    á
    tuma
    Date of purchase of gas oil
    vehicleRegistrationNumber -- Kereskedelmi j
    á
    rm
    ű
    forgalmi rendsz
    á
    ma (csak bet
    ű
    k
    é
    s sz
    á
    mok)
    Registration number of vehicle (letters and numbers only)
    dieselOilQuantity -- G
    é
    pi b
    é
    rmunka-szolg
    á
    ltat
    á
    s sor
    á
    n felhaszn
    á
    lt g
    á
    zolaj mennyis
    é
    ge literben
    –
    J
    ö
    t. 117.
    §
    (2)
    Ford
    í
    tand
    ó
    helyett: Quantity of diesel oil used for contract work and machinery hire service in liter
    –
    Act LXVIII of 2016 on Excise Tax section 117 (2)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, purchaseLocation=None, purchaseDate=None, vehicleRegistrationNumber=None, dieselOilQuantity=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.purchaseLocation = purchaseLocation
        self.purchaseLocation_nsprefix_ = "base"
        if isinstance(purchaseDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(purchaseDate, '%Y-%m-%d').date()
        else:
            initvalue_ = purchaseDate
        self.purchaseDate = initvalue_
        self.purchaseDate_nsprefix_ = "base"
        self.vehicleRegistrationNumber = vehicleRegistrationNumber
        self.validate_PlateNumberType(self.vehicleRegistrationNumber)
        self.vehicleRegistrationNumber_nsprefix_ = "common"
        self.dieselOilQuantity = dieselOilQuantity
        self.validate_QuantityType(self.dieselOilQuantity)
        self.dieselOilQuantity_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DieselOilPurchaseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DieselOilPurchaseType.subclass:
            return DieselOilPurchaseType.subclass(*args_, **kwargs_)
        else:
            return DieselOilPurchaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_purchaseLocation(self):
        return self.purchaseLocation
    def set_purchaseLocation(self, purchaseLocation):
        self.purchaseLocation = purchaseLocation
    def get_purchaseDate(self):
        return self.purchaseDate
    def set_purchaseDate(self, purchaseDate):
        self.purchaseDate = purchaseDate
    def get_vehicleRegistrationNumber(self):
        return self.vehicleRegistrationNumber
    def set_vehicleRegistrationNumber(self, vehicleRegistrationNumber):
        self.vehicleRegistrationNumber = vehicleRegistrationNumber
    def get_dieselOilQuantity(self):
        return self.dieselOilQuantity
    def set_dieselOilQuantity(self, dieselOilQuantity):
        self.dieselOilQuantity = dieselOilQuantity
    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceDateType_patterns_, ))
                result = False
        return result
    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]
    def validate_PlateNumberType(self, value):
        result = True
        # Validate type PlateNumberType, a restriction on AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PlateNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PlateNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PlateNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PlateNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_PlateNumberType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PlateNumberType_patterns_, ))
                result = False
        return result
    validate_PlateNumberType_patterns_ = [['^([A-Z0-9ÖŐÜŰ]{2,30})$']]
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.purchaseLocation is not None or
            self.purchaseDate is not None or
            self.vehicleRegistrationNumber is not None or
            self.dieselOilQuantity is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='DieselOilPurchaseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DieselOilPurchaseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DieselOilPurchaseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DieselOilPurchaseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DieselOilPurchaseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DieselOilPurchaseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='DieselOilPurchaseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.purchaseLocation is not None:
            namespaceprefix_ = self.purchaseLocation_nsprefix_ + ':' if (UseCapturedNS_ and self.purchaseLocation_nsprefix_) else ''
            self.purchaseLocation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='purchaseLocation', pretty_print=pretty_print)
        if self.purchaseDate is not None:
            namespaceprefix_ = self.purchaseDate_nsprefix_ + ':' if (UseCapturedNS_ and self.purchaseDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spurchaseDate>%s</%spurchaseDate>%s' % (namespaceprefix_ , self.gds_format_date(self.purchaseDate, input_name='purchaseDate'), namespaceprefix_ , eol_))
        if self.vehicleRegistrationNumber is not None:
            namespaceprefix_ = self.vehicleRegistrationNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.vehicleRegistrationNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svehicleRegistrationNumber>%s</%svehicleRegistrationNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.vehicleRegistrationNumber), input_name='vehicleRegistrationNumber')), namespaceprefix_ , eol_))
        if self.dieselOilQuantity is not None:
            namespaceprefix_ = self.dieselOilQuantity_nsprefix_ + ':' if (UseCapturedNS_ and self.dieselOilQuantity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdieselOilQuantity>%s</%sdieselOilQuantity>%s' % (namespaceprefix_ , self.gds_format_decimal(self.dieselOilQuantity, input_name='dieselOilQuantity'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='DieselOilPurchaseType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.purchaseLocation is not None:
            purchaseLocation_ = self.purchaseLocation
            purchaseLocation_.to_etree(element, name_='purchaseLocation', mapping_=mapping_, nsmap_=nsmap_)
        if self.purchaseDate is not None:
            purchaseDate_ = self.purchaseDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}purchaseDate').text = self.gds_format_date(purchaseDate_)
        if self.vehicleRegistrationNumber is not None:
            vehicleRegistrationNumber_ = self.vehicleRegistrationNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vehicleRegistrationNumber').text = self.gds_format_string(vehicleRegistrationNumber_)
        if self.dieselOilQuantity is not None:
            dieselOilQuantity_ = self.dieselOilQuantity
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}dieselOilQuantity').text = self.gds_format_decimal(dieselOilQuantity_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DieselOilPurchaseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.purchaseLocation is not None:
            showIndent(outfile, level)
            outfile.write('purchaseLocation=model_.SimpleAddressType(\n')
            self.purchaseLocation.exportLiteral(outfile, level, name_='purchaseLocation')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.purchaseDate is not None:
            showIndent(outfile, level)
            outfile.write('purchaseDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.purchaseDate, input_name='purchaseDate'))
        if self.vehicleRegistrationNumber is not None:
            showIndent(outfile, level)
            outfile.write('vehicleRegistrationNumber=%s,\n' % self.gds_encode(quote_python(self.vehicleRegistrationNumber)))
        if self.dieselOilQuantity is not None:
            showIndent(outfile, level)
            outfile.write('dieselOilQuantity=%f,\n' % self.dieselOilQuantity)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'purchaseLocation':
            obj_ = SimpleAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.purchaseLocation = obj_
            obj_.original_tagname_ = 'purchaseLocation'
        elif nodeName_ == 'purchaseDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.purchaseDate = dval_
            self.purchaseDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.purchaseDate)
        elif nodeName_ == 'vehicleRegistrationNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'vehicleRegistrationNumber')
            value_ = self.gds_validate_string(value_, node, 'vehicleRegistrationNumber')
            self.vehicleRegistrationNumber = value_
            self.vehicleRegistrationNumber_nsprefix_ = child_.prefix
            # validate type PlateNumberType
            self.validate_PlateNumberType(self.vehicleRegistrationNumber)
        elif nodeName_ == 'dieselOilQuantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'dieselOilQuantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'dieselOilQuantity')
            self.dieselOilQuantity = fval_
            self.dieselOilQuantity_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.dieselOilQuantity)
# end class DieselOilPurchaseType


class DiscountDataType(GeneratedsSuper):
    """DiscountDataType -- Á
    rengedm
    é
    ny adatok
    Discount data
    discountDescription -- Az
    á
    rengedm
    é
    ny le
    í
    r
    á
    sa
    Description of the discount
    discountValue -- T
    é
    telhez tartoz
    ó
    á
    rengedm
    é
    ny
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben, ha az egys
    é
    g
    á
    r nem tartalmazza
    Total amount of discount per item expressed in the currency of the invoice if not included in the unit price
    discountRate -- T
    é
    telhez tartoz
    ó
    á
    rengedm
    é
    ny ar
    á
    nya, ha az egys
    é
    g
    á
    r nem tartalmazza
    Rate of discount per item expressed in the currency of the invoice if not included in the unit price

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, discountDescription=None, discountValue=None, discountRate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.discountDescription = discountDescription
        self.validate_SimpleText255NotBlankType(self.discountDescription)
        self.discountDescription_nsprefix_ = "common"
        self.discountValue = discountValue
        self.validate_MonetaryType(self.discountValue)
        self.discountValue_nsprefix_ = "base"
        self.discountRate = discountRate
        self.validate_RateType(self.discountRate)
        self.discountRate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DiscountDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DiscountDataType.subclass:
            return DiscountDataType.subclass(*args_, **kwargs_)
        else:
            return DiscountDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_discountDescription(self):
        return self.discountDescription
    def set_discountDescription(self, discountDescription):
        self.discountDescription = discountDescription
    def get_discountValue(self):
        return self.discountValue
    def set_discountValue(self, discountValue):
        self.discountValue = discountValue
    def get_discountRate(self):
        return self.discountRate
    def set_discountRate(self, discountRate):
        self.discountRate = discountRate
    def validate_SimpleText255NotBlankType(self, value):
        result = True
        # Validate type SimpleText255NotBlankType, a restriction on AtomicStringType255.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText255NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText255NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText255NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText255NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText255NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_RateType(self, value):
        result = True
        # Validate type RateType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.discountDescription is not None or
            self.discountValue is not None or
            self.discountRate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='DiscountDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DiscountDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DiscountDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DiscountDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DiscountDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DiscountDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='DiscountDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.discountDescription is not None:
            namespaceprefix_ = self.discountDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.discountDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiscountDescription>%s</%sdiscountDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.discountDescription), input_name='discountDescription')), namespaceprefix_ , eol_))
        if self.discountValue is not None:
            namespaceprefix_ = self.discountValue_nsprefix_ + ':' if (UseCapturedNS_ and self.discountValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiscountValue>%s</%sdiscountValue>%s' % (namespaceprefix_ , self.gds_format_decimal(self.discountValue, input_name='discountValue'), namespaceprefix_ , eol_))
        if self.discountRate is not None:
            namespaceprefix_ = self.discountRate_nsprefix_ + ':' if (UseCapturedNS_ and self.discountRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiscountRate>%s</%sdiscountRate>%s' % (namespaceprefix_ , self.gds_format_decimal(self.discountRate, input_name='discountRate'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='DiscountDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.discountDescription is not None:
            discountDescription_ = self.discountDescription
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}discountDescription').text = self.gds_format_string(discountDescription_)
        if self.discountValue is not None:
            discountValue_ = self.discountValue
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}discountValue').text = self.gds_format_decimal(discountValue_)
        if self.discountRate is not None:
            discountRate_ = self.discountRate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}discountRate').text = self.gds_format_decimal(discountRate_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DiscountDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.discountDescription is not None:
            showIndent(outfile, level)
            outfile.write('discountDescription=%s,\n' % self.gds_encode(quote_python(self.discountDescription)))
        if self.discountValue is not None:
            showIndent(outfile, level)
            outfile.write('discountValue=%f,\n' % self.discountValue)
        if self.discountRate is not None:
            showIndent(outfile, level)
            outfile.write('discountRate=%f,\n' % self.discountRate)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'discountDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'discountDescription')
            value_ = self.gds_validate_string(value_, node, 'discountDescription')
            self.discountDescription = value_
            self.discountDescription_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.discountDescription)
        elif nodeName_ == 'discountValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'discountValue')
            fval_ = self.gds_validate_decimal(fval_, node, 'discountValue')
            self.discountValue = fval_
            self.discountValue_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.discountValue)
        elif nodeName_ == 'discountRate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'discountRate')
            fval_ = self.gds_validate_decimal(fval_, node, 'discountRate')
            self.discountRate = fval_
            self.discountRate_nsprefix_ = child_.prefix
            # validate type RateType
            self.validate_RateType(self.discountRate)
# end class DiscountDataType


class EkaerIdsType(GeneratedsSuper):
    """EkaerIdsType -- EK
    Á
    ER azonos
    í
    t
    ó
    (k)
    EKAER ID-s
    ekaerId -- EK
    Á
    ER azonos
    í
    t
    ó
    EKAER numbers; EKAER stands for Electronic Trade and Transport Control System

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ekaerId=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if ekaerId is None:
            self.ekaerId = []
        else:
            self.ekaerId = ekaerId
        self.ekaerId_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EkaerIdsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EkaerIdsType.subclass:
            return EkaerIdsType.subclass(*args_, **kwargs_)
        else:
            return EkaerIdsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ekaerId(self):
        return self.ekaerId
    def set_ekaerId(self, ekaerId):
        self.ekaerId = ekaerId
    def add_ekaerId(self, value):
        self.ekaerId.append(value)
    def insert_ekaerId_at(self, index, value):
        self.ekaerId.insert(index, value)
    def replace_ekaerId_at(self, index, value):
        self.ekaerId[index] = value
    def validate_EkaerIdType(self, value):
        result = True
        # Validate type EkaerIdType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EkaerIdType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on EkaerIdType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_EkaerIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_EkaerIdType_patterns_, ))
                result = False
        return result
    validate_EkaerIdType_patterns_ = [['^([E]{1}[0-9]{6}[0-9A-F]{8})$']]
    def _hasContent(self):
        if (
            self.ekaerId
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='EkaerIdsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EkaerIdsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EkaerIdsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EkaerIdsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EkaerIdsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EkaerIdsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='EkaerIdsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ekaerId_ in self.ekaerId:
            namespaceprefix_ = self.ekaerId_nsprefix_ + ':' if (UseCapturedNS_ and self.ekaerId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sekaerId>%s</%sekaerId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(ekaerId_), input_name='ekaerId')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='EkaerIdsType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for ekaerId_ in self.ekaerId:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}ekaerId').text = self.gds_format_string(ekaerId_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='EkaerIdsType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('ekaerId=[\n')
        level += 1
        for ekaerId_ in self.ekaerId:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(ekaerId_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ekaerId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ekaerId')
            value_ = self.gds_validate_string(value_, node, 'ekaerId')
            self.ekaerId.append(value_)
            self.ekaerId_nsprefix_ = child_.prefix
            # validate type EkaerIdType
            self.validate_EkaerIdType(self.ekaerId[-1])
# end class EkaerIdsType


class FiscalRepresentativeType(GeneratedsSuper):
    """FiscalRepresentativeType -- A p
    é
    nz
    ü
    gyi k
    é
    pvisel
    ő
    adatai
    Fiscal representative data
    fiscalRepresentativeTaxNumber -- A p
    é
    nz
    ü
    gyi k
    é
    pvisel
    ő
    ad
    ó
    sz
    á
    ma
    Tax number of the fiscal representative
    fiscalRepresentativeName -- A p
    é
    nz
    ü
    gyi k
    é
    pvisel
    ő
    neve
    Name of the fiscal representative
    fiscalRepresentativeAddress -- P
    é
    nz
    ü
    gyi k
    é
    pvisel
    ő
    c
    í
    me
    Address of the fiscal representative
    fiscalRepresentativeBankAccountNumber -- P
    é
    nz
    ü
    gyi k
    é
    pvisel
    ő
    á
    ltal a sz
    á
    mla kibocs
    á
    t
    ó
    (elad
    ó
    ) sz
    á
    m
    á
    ra megnyitott banksz
    á
    mla banksz
    á
    mlasz
    á
    ma
    Bank account number opened by the fiscal representative for the issuer of the invoice (supplier)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, fiscalRepresentativeTaxNumber=None, fiscalRepresentativeName=None, fiscalRepresentativeAddress=None, fiscalRepresentativeBankAccountNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.fiscalRepresentativeTaxNumber = fiscalRepresentativeTaxNumber
        self.fiscalRepresentativeTaxNumber_nsprefix_ = "base"
        self.fiscalRepresentativeName = fiscalRepresentativeName
        self.validate_SimpleText512NotBlankType(self.fiscalRepresentativeName)
        self.fiscalRepresentativeName_nsprefix_ = "common"
        self.fiscalRepresentativeAddress = fiscalRepresentativeAddress
        self.fiscalRepresentativeAddress_nsprefix_ = "base"
        self.fiscalRepresentativeBankAccountNumber = fiscalRepresentativeBankAccountNumber
        self.validate_BankAccountNumberType(self.fiscalRepresentativeBankAccountNumber)
        self.fiscalRepresentativeBankAccountNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FiscalRepresentativeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FiscalRepresentativeType.subclass:
            return FiscalRepresentativeType.subclass(*args_, **kwargs_)
        else:
            return FiscalRepresentativeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_fiscalRepresentativeTaxNumber(self):
        return self.fiscalRepresentativeTaxNumber
    def set_fiscalRepresentativeTaxNumber(self, fiscalRepresentativeTaxNumber):
        self.fiscalRepresentativeTaxNumber = fiscalRepresentativeTaxNumber
    def get_fiscalRepresentativeName(self):
        return self.fiscalRepresentativeName
    def set_fiscalRepresentativeName(self, fiscalRepresentativeName):
        self.fiscalRepresentativeName = fiscalRepresentativeName
    def get_fiscalRepresentativeAddress(self):
        return self.fiscalRepresentativeAddress
    def set_fiscalRepresentativeAddress(self, fiscalRepresentativeAddress):
        self.fiscalRepresentativeAddress = fiscalRepresentativeAddress
    def get_fiscalRepresentativeBankAccountNumber(self):
        return self.fiscalRepresentativeBankAccountNumber
    def set_fiscalRepresentativeBankAccountNumber(self, fiscalRepresentativeBankAccountNumber):
        self.fiscalRepresentativeBankAccountNumber = fiscalRepresentativeBankAccountNumber
    def validate_SimpleText512NotBlankType(self, value):
        result = True
        # Validate type SimpleText512NotBlankType, a restriction on AtomicStringType512.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText512NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText512NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText512NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText512NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText512NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_BankAccountNumberType(self, value):
        result = True
        # Validate type BankAccountNumberType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 34:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on BankAccountNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on BankAccountNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on BankAccountNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on BankAccountNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_BankAccountNumberType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_BankAccountNumberType_patterns_, ))
                result = False
        return result
    validate_BankAccountNumberType_patterns_ = [['^([0-9]{8}[-][0-9]{8}[-][0-9]{8}|[0-9]{8}[-][0-9]{8}|[A-Z]{2}[0-9]{2}[0-9A-Za-z]{11,30})$']]
    def _hasContent(self):
        if (
            self.fiscalRepresentativeTaxNumber is not None or
            self.fiscalRepresentativeName is not None or
            self.fiscalRepresentativeAddress is not None or
            self.fiscalRepresentativeBankAccountNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='FiscalRepresentativeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FiscalRepresentativeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FiscalRepresentativeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FiscalRepresentativeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FiscalRepresentativeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FiscalRepresentativeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='FiscalRepresentativeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.fiscalRepresentativeTaxNumber is not None:
            namespaceprefix_ = self.fiscalRepresentativeTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.fiscalRepresentativeTaxNumber_nsprefix_) else ''
            self.fiscalRepresentativeTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='fiscalRepresentativeTaxNumber', pretty_print=pretty_print)
        if self.fiscalRepresentativeName is not None:
            namespaceprefix_ = self.fiscalRepresentativeName_nsprefix_ + ':' if (UseCapturedNS_ and self.fiscalRepresentativeName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfiscalRepresentativeName>%s</%sfiscalRepresentativeName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.fiscalRepresentativeName), input_name='fiscalRepresentativeName')), namespaceprefix_ , eol_))
        if self.fiscalRepresentativeAddress is not None:
            namespaceprefix_ = self.fiscalRepresentativeAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.fiscalRepresentativeAddress_nsprefix_) else ''
            self.fiscalRepresentativeAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='fiscalRepresentativeAddress', pretty_print=pretty_print)
        if self.fiscalRepresentativeBankAccountNumber is not None:
            namespaceprefix_ = self.fiscalRepresentativeBankAccountNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.fiscalRepresentativeBankAccountNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfiscalRepresentativeBankAccountNumber>%s</%sfiscalRepresentativeBankAccountNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.fiscalRepresentativeBankAccountNumber), input_name='fiscalRepresentativeBankAccountNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='FiscalRepresentativeType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.fiscalRepresentativeTaxNumber is not None:
            fiscalRepresentativeTaxNumber_ = self.fiscalRepresentativeTaxNumber
            fiscalRepresentativeTaxNumber_.to_etree(element, name_='fiscalRepresentativeTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if self.fiscalRepresentativeName is not None:
            fiscalRepresentativeName_ = self.fiscalRepresentativeName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}fiscalRepresentativeName').text = self.gds_format_string(fiscalRepresentativeName_)
        if self.fiscalRepresentativeAddress is not None:
            fiscalRepresentativeAddress_ = self.fiscalRepresentativeAddress
            fiscalRepresentativeAddress_.to_etree(element, name_='fiscalRepresentativeAddress', mapping_=mapping_, nsmap_=nsmap_)
        if self.fiscalRepresentativeBankAccountNumber is not None:
            fiscalRepresentativeBankAccountNumber_ = self.fiscalRepresentativeBankAccountNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}fiscalRepresentativeBankAccountNumber').text = self.gds_format_string(fiscalRepresentativeBankAccountNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='FiscalRepresentativeType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.fiscalRepresentativeTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('fiscalRepresentativeTaxNumber=model_.TaxNumberType(\n')
            self.fiscalRepresentativeTaxNumber.exportLiteral(outfile, level, name_='fiscalRepresentativeTaxNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fiscalRepresentativeName is not None:
            showIndent(outfile, level)
            outfile.write('fiscalRepresentativeName=%s,\n' % self.gds_encode(quote_python(self.fiscalRepresentativeName)))
        if self.fiscalRepresentativeAddress is not None:
            showIndent(outfile, level)
            outfile.write('fiscalRepresentativeAddress=model_.AddressType(\n')
            self.fiscalRepresentativeAddress.exportLiteral(outfile, level, name_='fiscalRepresentativeAddress')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.fiscalRepresentativeBankAccountNumber is not None:
            showIndent(outfile, level)
            outfile.write('fiscalRepresentativeBankAccountNumber=%s,\n' % self.gds_encode(quote_python(self.fiscalRepresentativeBankAccountNumber)))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'fiscalRepresentativeTaxNumber':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.fiscalRepresentativeTaxNumber = obj_
            obj_.original_tagname_ = 'fiscalRepresentativeTaxNumber'
        elif nodeName_ == 'fiscalRepresentativeName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fiscalRepresentativeName')
            value_ = self.gds_validate_string(value_, node, 'fiscalRepresentativeName')
            self.fiscalRepresentativeName = value_
            self.fiscalRepresentativeName_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.fiscalRepresentativeName)
        elif nodeName_ == 'fiscalRepresentativeAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.fiscalRepresentativeAddress = obj_
            obj_.original_tagname_ = 'fiscalRepresentativeAddress'
        elif nodeName_ == 'fiscalRepresentativeBankAccountNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fiscalRepresentativeBankAccountNumber')
            value_ = self.gds_validate_string(value_, node, 'fiscalRepresentativeBankAccountNumber')
            self.fiscalRepresentativeBankAccountNumber = value_
            self.fiscalRepresentativeBankAccountNumber_nsprefix_ = child_.prefix
            # validate type BankAccountNumberType
            self.validate_BankAccountNumberType(self.fiscalRepresentativeBankAccountNumber)
# end class FiscalRepresentativeType


class GeneralLedgerAccountNumbersType(GeneratedsSuper):
    """GeneralLedgerAccountNumbersType -- F
    ő
    k
    ö
    nyvi sz
    á
    mlasz
    á
    mok
    General ledger account numbers
    generalLedgerAccountNumber -- F
    ő
    k
    ö
    nyvi sz
    á
    mlasz
    á
    m
    General ledger account number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, generalLedgerAccountNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if generalLedgerAccountNumber is None:
            self.generalLedgerAccountNumber = []
        else:
            self.generalLedgerAccountNumber = generalLedgerAccountNumber
        self.generalLedgerAccountNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GeneralLedgerAccountNumbersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GeneralLedgerAccountNumbersType.subclass:
            return GeneralLedgerAccountNumbersType.subclass(*args_, **kwargs_)
        else:
            return GeneralLedgerAccountNumbersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_generalLedgerAccountNumber(self):
        return self.generalLedgerAccountNumber
    def set_generalLedgerAccountNumber(self, generalLedgerAccountNumber):
        self.generalLedgerAccountNumber = generalLedgerAccountNumber
    def add_generalLedgerAccountNumber(self, value):
        self.generalLedgerAccountNumber.append(value)
    def insert_generalLedgerAccountNumber_at(self, index, value):
        self.generalLedgerAccountNumber.insert(index, value)
    def replace_generalLedgerAccountNumber_at(self, index, value):
        self.generalLedgerAccountNumber[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.generalLedgerAccountNumber
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='GeneralLedgerAccountNumbersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GeneralLedgerAccountNumbersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GeneralLedgerAccountNumbersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GeneralLedgerAccountNumbersType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GeneralLedgerAccountNumbersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GeneralLedgerAccountNumbersType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='GeneralLedgerAccountNumbersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for generalLedgerAccountNumber_ in self.generalLedgerAccountNumber:
            namespaceprefix_ = self.generalLedgerAccountNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.generalLedgerAccountNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgeneralLedgerAccountNumber>%s</%sgeneralLedgerAccountNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(generalLedgerAccountNumber_), input_name='generalLedgerAccountNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='GeneralLedgerAccountNumbersType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for generalLedgerAccountNumber_ in self.generalLedgerAccountNumber:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}generalLedgerAccountNumber').text = self.gds_format_string(generalLedgerAccountNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='GeneralLedgerAccountNumbersType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('generalLedgerAccountNumber=[\n')
        level += 1
        for generalLedgerAccountNumber_ in self.generalLedgerAccountNumber:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(generalLedgerAccountNumber_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'generalLedgerAccountNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'generalLedgerAccountNumber')
            value_ = self.gds_validate_string(value_, node, 'generalLedgerAccountNumber')
            self.generalLedgerAccountNumber.append(value_)
            self.generalLedgerAccountNumber_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.generalLedgerAccountNumber[-1])
# end class GeneralLedgerAccountNumbersType


class GlnNumbersType(GeneratedsSuper):
    """GlnNumbersType -- Glob
    á
    lis helyazonos
    í
    t
    ó
    sz
    á
    mok
    Global location numbers
    glnNumber -- Glob
    á
    lis helyazonos
    í
    t
    ó
    sz
    á
    m
    Global location number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, glnNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if glnNumber is None:
            self.glnNumber = []
        else:
            self.glnNumber = glnNumber
        self.glnNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GlnNumbersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GlnNumbersType.subclass:
            return GlnNumbersType.subclass(*args_, **kwargs_)
        else:
            return GlnNumbersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_glnNumber(self):
        return self.glnNumber
    def set_glnNumber(self, glnNumber):
        self.glnNumber = glnNumber
    def add_glnNumber(self, value):
        self.glnNumber.append(value)
    def insert_glnNumber_at(self, index, value):
        self.glnNumber.insert(index, value)
    def replace_glnNumber_at(self, index, value):
        self.glnNumber[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.glnNumber
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='GlnNumbersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GlnNumbersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GlnNumbersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GlnNumbersType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GlnNumbersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GlnNumbersType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='GlnNumbersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for glnNumber_ in self.glnNumber:
            namespaceprefix_ = self.glnNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.glnNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sglnNumber>%s</%sglnNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(glnNumber_), input_name='glnNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='GlnNumbersType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for glnNumber_ in self.glnNumber:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}glnNumber').text = self.gds_format_string(glnNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='GlnNumbersType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('glnNumber=[\n')
        level += 1
        for glnNumber_ in self.glnNumber:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(glnNumber_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'glnNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'glnNumber')
            value_ = self.gds_validate_string(value_, node, 'glnNumber')
            self.glnNumber.append(value_)
            self.glnNumber_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.glnNumber[-1])
# end class GlnNumbersType




# end class InvoiceDataType


# end class InvoiceHeadType


# end class InvoiceMainType


# end class InvoiceReferenceType


# end class InvoiceType


class ItemNumbersType(GeneratedsSuper):
    """ItemNumbersType -- Cikksz
    á
    mok
    Item numbers
    itemNumber -- Cikksz
    á
    m
    Item number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, itemNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if itemNumber is None:
            self.itemNumber = []
        else:
            self.itemNumber = itemNumber
        self.itemNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ItemNumbersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ItemNumbersType.subclass:
            return ItemNumbersType.subclass(*args_, **kwargs_)
        else:
            return ItemNumbersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_itemNumber(self):
        return self.itemNumber
    def set_itemNumber(self, itemNumber):
        self.itemNumber = itemNumber
    def add_itemNumber(self, value):
        self.itemNumber.append(value)
    def insert_itemNumber_at(self, index, value):
        self.itemNumber.insert(index, value)
    def replace_itemNumber_at(self, index, value):
        self.itemNumber[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.itemNumber
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ItemNumbersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ItemNumbersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ItemNumbersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ItemNumbersType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ItemNumbersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ItemNumbersType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ItemNumbersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for itemNumber_ in self.itemNumber:
            namespaceprefix_ = self.itemNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.itemNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sitemNumber>%s</%sitemNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(itemNumber_), input_name='itemNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ItemNumbersType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for itemNumber_ in self.itemNumber:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}itemNumber').text = self.gds_format_string(itemNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ItemNumbersType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('itemNumber=[\n')
        level += 1
        for itemNumber_ in self.itemNumber:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(itemNumber_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'itemNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'itemNumber')
            value_ = self.gds_validate_string(value_, node, 'itemNumber')
            self.itemNumber.append(value_)
            self.itemNumber_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.itemNumber[-1])
# end class ItemNumbersType


class LineAmountsNormalType(GeneratedsSuper):
    """LineAmountsNormalType -- Norm
    á
    l vagy gy
    ű
    jt
    ő
    sz
    á
    mla eset
    é
    n kit
    ö
    ltend
    ő
    t
    é
    tel
    é
    rt
    é
    k adatok
    Item value data to be completed in case of normal or aggregate invoice
    lineNetAmountData -- T
    é
    tel nett
    ó
    adatok
    Line net data
    lineVatRate -- Ad
    ó
    m
    é
    rt
    é
    k vagy ad
    ó
    mentess
    é
    g jel
    ö
    l
    é
    se
    Tax rate or tax exemption marking
    lineVatData -- T
    é
    tel
    Á
    FA adatok
    Line VAT data
    lineGrossAmountData -- T
    é
    tel brutt
    ó
    adatok
    Line gross data

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineNetAmountData=None, lineVatRate=None, lineVatData=None, lineGrossAmountData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineNetAmountData = lineNetAmountData
        self.lineNetAmountData_nsprefix_ = None
        self.lineVatRate = lineVatRate
        self.lineVatRate_nsprefix_ = None
        self.lineVatData = lineVatData
        self.lineVatData_nsprefix_ = None
        self.lineGrossAmountData = lineGrossAmountData
        self.lineGrossAmountData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineAmountsNormalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineAmountsNormalType.subclass:
            return LineAmountsNormalType.subclass(*args_, **kwargs_)
        else:
            return LineAmountsNormalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineNetAmountData(self):
        return self.lineNetAmountData
    def set_lineNetAmountData(self, lineNetAmountData):
        self.lineNetAmountData = lineNetAmountData
    def get_lineVatRate(self):
        return self.lineVatRate
    def set_lineVatRate(self, lineVatRate):
        self.lineVatRate = lineVatRate
    def get_lineVatData(self):
        return self.lineVatData
    def set_lineVatData(self, lineVatData):
        self.lineVatData = lineVatData
    def get_lineGrossAmountData(self):
        return self.lineGrossAmountData
    def set_lineGrossAmountData(self, lineGrossAmountData):
        self.lineGrossAmountData = lineGrossAmountData
    def _hasContent(self):
        if (
            self.lineNetAmountData is not None or
            self.lineVatRate is not None or
            self.lineVatData is not None or
            self.lineGrossAmountData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LineAmountsNormalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineAmountsNormalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineAmountsNormalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineAmountsNormalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineAmountsNormalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineAmountsNormalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LineAmountsNormalType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineNetAmountData is not None:
            namespaceprefix_ = self.lineNetAmountData_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNetAmountData_nsprefix_) else ''
            self.lineNetAmountData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineNetAmountData', pretty_print=pretty_print)
        if self.lineVatRate is not None:
            namespaceprefix_ = self.lineVatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatRate_nsprefix_) else ''
            self.lineVatRate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineVatRate', pretty_print=pretty_print)
        if self.lineVatData is not None:
            namespaceprefix_ = self.lineVatData_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatData_nsprefix_) else ''
            self.lineVatData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineVatData', pretty_print=pretty_print)
        if self.lineGrossAmountData is not None:
            namespaceprefix_ = self.lineGrossAmountData_nsprefix_ + ':' if (UseCapturedNS_ and self.lineGrossAmountData_nsprefix_) else ''
            self.lineGrossAmountData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineGrossAmountData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='LineAmountsNormalType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineNetAmountData is not None:
            lineNetAmountData_ = self.lineNetAmountData
            lineNetAmountData_.to_etree(element, name_='lineNetAmountData', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineVatRate is not None:
            lineVatRate_ = self.lineVatRate
            lineVatRate_.to_etree(element, name_='lineVatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineVatData is not None:
            lineVatData_ = self.lineVatData
            lineVatData_.to_etree(element, name_='lineVatData', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineGrossAmountData is not None:
            lineGrossAmountData_ = self.lineGrossAmountData
            lineGrossAmountData_.to_etree(element, name_='lineGrossAmountData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineAmountsNormalType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineNetAmountData is not None:
            showIndent(outfile, level)
            outfile.write('lineNetAmountData=model_.LineNetAmountDataType(\n')
            self.lineNetAmountData.exportLiteral(outfile, level, name_='lineNetAmountData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineVatRate is not None:
            showIndent(outfile, level)
            outfile.write('lineVatRate=model_.VatRateType(\n')
            self.lineVatRate.exportLiteral(outfile, level, name_='lineVatRate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineVatData is not None:
            showIndent(outfile, level)
            outfile.write('lineVatData=model_.LineVatDataType(\n')
            self.lineVatData.exportLiteral(outfile, level, name_='lineVatData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineGrossAmountData is not None:
            showIndent(outfile, level)
            outfile.write('lineGrossAmountData=model_.LineGrossAmountDataType(\n')
            self.lineGrossAmountData.exportLiteral(outfile, level, name_='lineGrossAmountData')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'lineNetAmountData':
            obj_ = LineNetAmountDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineNetAmountData = obj_
            obj_.original_tagname_ = 'lineNetAmountData'
        elif nodeName_ == 'lineVatRate':
            obj_ = VatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineVatRate = obj_
            obj_.original_tagname_ = 'lineVatRate'
        elif nodeName_ == 'lineVatData':
            obj_ = LineVatDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineVatData = obj_
            obj_.original_tagname_ = 'lineVatData'
        elif nodeName_ == 'lineGrossAmountData':
            obj_ = LineGrossAmountDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineGrossAmountData = obj_
            obj_.original_tagname_ = 'lineGrossAmountData'
# end class LineAmountsNormalType


class LineAmountsSimplifiedType(GeneratedsSuper):
    """LineAmountsSimplifiedType -- Egyszer
    ű
    s
    í
    tett sz
    á
    mla eset
    é
    n kit
    ö
    ltend
    ő
    t
    é
    tel
    é
    rt
    é
    k adatok
    Item value data to be completed in case of simplified invoice
    lineVatRate -- Ad
    ó
    m
    é
    rt
    é
    k vagy ad
    ó
    mentess
    é
    g jel
    ö
    l
    é
    se
    Tax rate or tax exemption marking
    lineGrossAmountSimplified -- T
    é
    tel brutt
    ó
    é
    rt
    é
    ke a sz
    á
    mla p
    é
    nznem
    é
    ben
    Gross amount of the item expressed in the currency of the invoice
    lineGrossAmountSimplifiedHUF -- T
    é
    tel brutt
    ó
    é
    rt
    é
    ke forintban
    Gross amount of the item expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineVatRate=None, lineGrossAmountSimplified=None, lineGrossAmountSimplifiedHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineVatRate = lineVatRate
        self.lineVatRate_nsprefix_ = None
        self.lineGrossAmountSimplified = lineGrossAmountSimplified
        self.validate_MonetaryType(self.lineGrossAmountSimplified)
        self.lineGrossAmountSimplified_nsprefix_ = "base"
        self.lineGrossAmountSimplifiedHUF = lineGrossAmountSimplifiedHUF
        self.validate_MonetaryType(self.lineGrossAmountSimplifiedHUF)
        self.lineGrossAmountSimplifiedHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineAmountsSimplifiedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineAmountsSimplifiedType.subclass:
            return LineAmountsSimplifiedType.subclass(*args_, **kwargs_)
        else:
            return LineAmountsSimplifiedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineVatRate(self):
        return self.lineVatRate
    def set_lineVatRate(self, lineVatRate):
        self.lineVatRate = lineVatRate
    def get_lineGrossAmountSimplified(self):
        return self.lineGrossAmountSimplified
    def set_lineGrossAmountSimplified(self, lineGrossAmountSimplified):
        self.lineGrossAmountSimplified = lineGrossAmountSimplified
    def get_lineGrossAmountSimplifiedHUF(self):
        return self.lineGrossAmountSimplifiedHUF
    def set_lineGrossAmountSimplifiedHUF(self, lineGrossAmountSimplifiedHUF):
        self.lineGrossAmountSimplifiedHUF = lineGrossAmountSimplifiedHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.lineVatRate is not None or
            self.lineGrossAmountSimplified is not None or
            self.lineGrossAmountSimplifiedHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineAmountsSimplifiedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineAmountsSimplifiedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineAmountsSimplifiedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineAmountsSimplifiedType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineAmountsSimplifiedType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineAmountsSimplifiedType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineAmountsSimplifiedType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineVatRate is not None:
            namespaceprefix_ = self.lineVatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatRate_nsprefix_) else ''
            self.lineVatRate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineVatRate', pretty_print=pretty_print)
        if self.lineGrossAmountSimplified is not None:
            namespaceprefix_ = self.lineGrossAmountSimplified_nsprefix_ + ':' if (UseCapturedNS_ and self.lineGrossAmountSimplified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineGrossAmountSimplified>%s</%slineGrossAmountSimplified>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineGrossAmountSimplified, input_name='lineGrossAmountSimplified'), namespaceprefix_ , eol_))
        if self.lineGrossAmountSimplifiedHUF is not None:
            namespaceprefix_ = self.lineGrossAmountSimplifiedHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.lineGrossAmountSimplifiedHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineGrossAmountSimplifiedHUF>%s</%slineGrossAmountSimplifiedHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineGrossAmountSimplifiedHUF, input_name='lineGrossAmountSimplifiedHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='LineAmountsSimplifiedType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineVatRate is not None:
            lineVatRate_ = self.lineVatRate
            lineVatRate_.to_etree(element, name_='lineVatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineGrossAmountSimplified is not None:
            lineGrossAmountSimplified_ = self.lineGrossAmountSimplified
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountSimplified').text = self.gds_format_decimal(lineGrossAmountSimplified_)
        if self.lineGrossAmountSimplifiedHUF is not None:
            lineGrossAmountSimplifiedHUF_ = self.lineGrossAmountSimplifiedHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountSimplifiedHUF').text = self.gds_format_decimal(lineGrossAmountSimplifiedHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineAmountsSimplifiedType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineVatRate is not None:
            showIndent(outfile, level)
            outfile.write('lineVatRate=model_.VatRateType(\n')
            self.lineVatRate.exportLiteral(outfile, level, name_='lineVatRate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineGrossAmountSimplified is not None:
            showIndent(outfile, level)
            outfile.write('lineGrossAmountSimplified=%f,\n' % self.lineGrossAmountSimplified)
        if self.lineGrossAmountSimplifiedHUF is not None:
            showIndent(outfile, level)
            outfile.write('lineGrossAmountSimplifiedHUF=%f,\n' % self.lineGrossAmountSimplifiedHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'lineVatRate':
            obj_ = VatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineVatRate = obj_
            obj_.original_tagname_ = 'lineVatRate'
        elif nodeName_ == 'lineGrossAmountSimplified' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineGrossAmountSimplified')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineGrossAmountSimplified')
            self.lineGrossAmountSimplified = fval_
            self.lineGrossAmountSimplified_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineGrossAmountSimplified)
        elif nodeName_ == 'lineGrossAmountSimplifiedHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineGrossAmountSimplifiedHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineGrossAmountSimplifiedHUF')
            self.lineGrossAmountSimplifiedHUF = fval_
            self.lineGrossAmountSimplifiedHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineGrossAmountSimplifiedHUF)
# end class LineAmountsSimplifiedType


class LineGrossAmountDataType(GeneratedsSuper):
    """LineGrossAmountDataType -- T
    é
    tel brutt
    ó
    adatok
    Line gross data
    lineGrossAmountNormal -- T
    é
    tel brutt
    ó
    é
    rt
    é
    ke a sz
    á
    mla p
    é
    nznem
    é
    ben.
    Á
    FA tartalm
    ú
    k
    ü
    l
    ö
    nb
    ö
    zeti ad
    ó
    z
    á
    s eset
    é
    n az ellen
    é
    rt
    é
    k.
    Gross amount of the item expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of consideration expressed in the currency of the invoice.
    lineGrossAmountNormalHUF -- T
    é
    tel brutt
    ó
    é
    rt
    é
    ke forintban
    Gross amount of the item expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineGrossAmountNormal=None, lineGrossAmountNormalHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineGrossAmountNormal = lineGrossAmountNormal
        self.validate_MonetaryType(self.lineGrossAmountNormal)
        self.lineGrossAmountNormal_nsprefix_ = "base"
        self.lineGrossAmountNormalHUF = lineGrossAmountNormalHUF
        self.validate_MonetaryType(self.lineGrossAmountNormalHUF)
        self.lineGrossAmountNormalHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineGrossAmountDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineGrossAmountDataType.subclass:
            return LineGrossAmountDataType.subclass(*args_, **kwargs_)
        else:
            return LineGrossAmountDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineGrossAmountNormal(self):
        return self.lineGrossAmountNormal
    def set_lineGrossAmountNormal(self, lineGrossAmountNormal):
        self.lineGrossAmountNormal = lineGrossAmountNormal
    def get_lineGrossAmountNormalHUF(self):
        return self.lineGrossAmountNormalHUF
    def set_lineGrossAmountNormalHUF(self, lineGrossAmountNormalHUF):
        self.lineGrossAmountNormalHUF = lineGrossAmountNormalHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.lineGrossAmountNormal is not None or
            self.lineGrossAmountNormalHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineGrossAmountDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineGrossAmountDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineGrossAmountDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineGrossAmountDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineGrossAmountDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineGrossAmountDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineGrossAmountDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineGrossAmountNormal is not None:
            namespaceprefix_ = self.lineGrossAmountNormal_nsprefix_ + ':' if (UseCapturedNS_ and self.lineGrossAmountNormal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineGrossAmountNormal>%s</%slineGrossAmountNormal>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineGrossAmountNormal, input_name='lineGrossAmountNormal'), namespaceprefix_ , eol_))
        if self.lineGrossAmountNormalHUF is not None:
            namespaceprefix_ = self.lineGrossAmountNormalHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.lineGrossAmountNormalHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineGrossAmountNormalHUF>%s</%slineGrossAmountNormalHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineGrossAmountNormalHUF, input_name='lineGrossAmountNormalHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='LineGrossAmountDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineGrossAmountNormal is not None:
            lineGrossAmountNormal_ = self.lineGrossAmountNormal
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountNormal').text = self.gds_format_decimal(lineGrossAmountNormal_)
        if self.lineGrossAmountNormalHUF is not None:
            lineGrossAmountNormalHUF_ = self.lineGrossAmountNormalHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineGrossAmountNormalHUF').text = self.gds_format_decimal(lineGrossAmountNormalHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineGrossAmountDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineGrossAmountNormal is not None:
            showIndent(outfile, level)
            outfile.write('lineGrossAmountNormal=%f,\n' % self.lineGrossAmountNormal)
        if self.lineGrossAmountNormalHUF is not None:
            showIndent(outfile, level)
            outfile.write('lineGrossAmountNormalHUF=%f,\n' % self.lineGrossAmountNormalHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'lineGrossAmountNormal' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineGrossAmountNormal')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineGrossAmountNormal')
            self.lineGrossAmountNormal = fval_
            self.lineGrossAmountNormal_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineGrossAmountNormal)
        elif nodeName_ == 'lineGrossAmountNormalHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineGrossAmountNormalHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineGrossAmountNormalHUF')
            self.lineGrossAmountNormalHUF = fval_
            self.lineGrossAmountNormalHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineGrossAmountNormalHUF)
# end class LineGrossAmountDataType


class LineModificationReferenceType(GeneratedsSuper):
    """LineModificationReferenceType -- M
    ó
    dos
    í
    t
    á
    sr
    ó
    l t
    ö
    rt
    é
    n
    ő
    adatszolg
    á
    ltat
    á
    s eset
    é
    n a t
    é
    telsor m
    ó
    dos
    í
    t
    á
    s jelleg
    é
    nek jel
    ö
    l
    é
    se
    Marking the goal of modification of the line (in the case of data supply about changes/updates only)
    lineNumberReference -- Az eredeti sz
    á
    mla m
    ó
    dos
    í
    t
    á
    ssal
    é
    rintett t
    é
    tel
    é
    nek sorsz
    á
    ma (lineNumber).
    Ú
    j t
    é
    tel l
    é
    trehoz
    á
    sa eset
    é
    n az
    ú
    j t
    é
    tel sorsz
    á
    ma, a megl
    é
    v
    ő
    t
    é
    telsorok sz
    á
    moz
    á
    s
    á
    nak folytat
    á
    sak
    é
    nt
    Line number of the original invoice, which the modification occurs with. In case of create operation the tag shall contain the new line number, as a sequential increment of the the existing lines set
    lineOperation -- A sz
    á
    mlat
    é
    tel m
    ó
    dos
    í
    t
    á
    s
    á
    nak jellege
    Line modification type

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineNumberReference=None, lineOperation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineNumberReference = lineNumberReference
        self.validate_LineNumberType(self.lineNumberReference)
        self.lineNumberReference_nsprefix_ = "base"
        self.lineOperation = lineOperation
        self.validate_LineOperationType(self.lineOperation)
        self.lineOperation_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineModificationReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineModificationReferenceType.subclass:
            return LineModificationReferenceType.subclass(*args_, **kwargs_)
        else:
            return LineModificationReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineNumberReference(self):
        return self.lineNumberReference
    def set_lineNumberReference(self, lineNumberReference):
        self.lineNumberReference = lineNumberReference
    def get_lineOperation(self):
        return self.lineOperation
    def set_lineOperation(self, lineOperation):
        self.lineOperation = lineOperation
    def validate_LineNumberType(self, value):
        result = True
        # Validate type LineNumberType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_LineOperationType(self, value):
        result = True
        # Validate type LineOperationType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['CREATE', 'MODIFY']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LineOperationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LineOperationType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LineOperationType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.lineNumberReference is not None or
            self.lineOperation is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LineModificationReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineModificationReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineModificationReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineModificationReferenceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineModificationReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineModificationReferenceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LineModificationReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineNumberReference is not None:
            namespaceprefix_ = self.lineNumberReference_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNumberReference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNumberReference>%s</%slineNumberReference>%s' % (namespaceprefix_ , self.gds_format_integer(self.lineNumberReference, input_name='lineNumberReference'), namespaceprefix_ , eol_))
        if self.lineOperation is not None:
            namespaceprefix_ = self.lineOperation_nsprefix_ + ':' if (UseCapturedNS_ and self.lineOperation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineOperation>%s</%slineOperation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lineOperation), input_name='lineOperation')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='LineModificationReferenceType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineNumberReference is not None:
            lineNumberReference_ = self.lineNumberReference
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineNumberReference').text = self.gds_format_integer(lineNumberReference_)
        if self.lineOperation is not None:
            lineOperation_ = self.lineOperation
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineOperation').text = self.gds_format_string(lineOperation_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineModificationReferenceType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineNumberReference is not None:
            showIndent(outfile, level)
            outfile.write('lineNumberReference=%d,\n' % self.lineNumberReference)
        if self.lineOperation is not None:
            showIndent(outfile, level)
            outfile.write('lineOperation=%s,\n' % self.gds_encode(quote_python(self.lineOperation)))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'lineNumberReference' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'lineNumberReference')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'lineNumberReference')
            self.lineNumberReference = ival_
            self.lineNumberReference_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.lineNumberReference)
        elif nodeName_ == 'lineOperation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lineOperation')
            value_ = self.gds_validate_string(value_, node, 'lineOperation')
            self.lineOperation = value_
            self.lineOperation_nsprefix_ = child_.prefix
            # validate type LineOperationType
            self.validate_LineOperationType(self.lineOperation)
# end class LineModificationReferenceType


class LineNetAmountDataType(GeneratedsSuper):
    """LineNetAmountDataType -- T
    é
    tel nett
    ó
    adatok
    Line net data
    lineNetAmount -- T
    é
    tel nett
    ó
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben.
    Á
    FA tartalm
    ú
    k
    ü
    l
    ö
    nb
    ö
    zeti ad
    ó
    z
    á
    s eset
    é
    n az ellen
    é
    rt
    é
    k
    á
    fa
    ö
    sszeg
    é
    vel cs
    ö
    kkentett
    é
    rt
    é
    ke a sz
    á
    mla p
    é
    nznem
    é
    ben.
    Net amount of the item expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of consideration reduced with the amount of VAT, expressed in the currency of the invoice.
    lineNetAmountHUF -- T
    é
    tel nett
    ó
    ö
    sszege forintban.
    Á
    FA tartalm
    ú
    k
    ü
    l
    ö
    nb
    ö
    zeti ad
    ó
    z
    á
    s eset
    é
    n az ellen
    é
    rt
    é
    k
    á
    fa
    ö
    sszeg
    é
    vel cs
    ö
    kkentett
    é
    rt
    é
    ke forintban.
    Net amount of the item expressed in HUF. Net amount of the item expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of consideration reduced with the amount of VAT, expressed in HUF.

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineNetAmount=None, lineNetAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineNetAmount = lineNetAmount
        self.validate_MonetaryType(self.lineNetAmount)
        self.lineNetAmount_nsprefix_ = "base"
        self.lineNetAmountHUF = lineNetAmountHUF
        self.validate_MonetaryType(self.lineNetAmountHUF)
        self.lineNetAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineNetAmountDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineNetAmountDataType.subclass:
            return LineNetAmountDataType.subclass(*args_, **kwargs_)
        else:
            return LineNetAmountDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineNetAmount(self):
        return self.lineNetAmount
    def set_lineNetAmount(self, lineNetAmount):
        self.lineNetAmount = lineNetAmount
    def get_lineNetAmountHUF(self):
        return self.lineNetAmountHUF
    def set_lineNetAmountHUF(self, lineNetAmountHUF):
        self.lineNetAmountHUF = lineNetAmountHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.lineNetAmount is not None or
            self.lineNetAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineNetAmountDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineNetAmountDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineNetAmountDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineNetAmountDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineNetAmountDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineNetAmountDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineNetAmountDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineNetAmount is not None:
            namespaceprefix_ = self.lineNetAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNetAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNetAmount>%s</%slineNetAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineNetAmount, input_name='lineNetAmount'), namespaceprefix_ , eol_))
        if self.lineNetAmountHUF is not None:
            namespaceprefix_ = self.lineNetAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNetAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNetAmountHUF>%s</%slineNetAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineNetAmountHUF, input_name='lineNetAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='LineNetAmountDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineNetAmount is not None:
            lineNetAmount_ = self.lineNetAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineNetAmount').text = self.gds_format_decimal(lineNetAmount_)
        if self.lineNetAmountHUF is not None:
            lineNetAmountHUF_ = self.lineNetAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineNetAmountHUF').text = self.gds_format_decimal(lineNetAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineNetAmountDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineNetAmount is not None:
            showIndent(outfile, level)
            outfile.write('lineNetAmount=%f,\n' % self.lineNetAmount)
        if self.lineNetAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('lineNetAmountHUF=%f,\n' % self.lineNetAmountHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'lineNetAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineNetAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineNetAmount')
            self.lineNetAmount = fval_
            self.lineNetAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineNetAmount)
        elif nodeName_ == 'lineNetAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineNetAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineNetAmountHUF')
            self.lineNetAmountHUF = fval_
            self.lineNetAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineNetAmountHUF)
# end class LineNetAmountDataType


class LinesType(GeneratedsSuper):
    """LinesType -- Term
    é
    k/szolg
    á
    ltat
    á
    s t
    é
    telek
    Product / service items
    mergedItemIndicator -- Jel
    ö
    li, ha az adatszolg
    á
    ltat
    á
    s m
    é
    retcs
    ö
    kkent
    é
    s miatt
    ö
    sszevont soradatokat tartalmaz
    Indicates whether the data exchange contains merged line data due to size reduction
    line -- Term
    é
    k/szolg
    á
    ltat
    á
    s t
    é
    tel
    Product / service item

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, mergedItemIndicator=None, line=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.mergedItemIndicator = mergedItemIndicator
        self.mergedItemIndicator_nsprefix_ = "xs"
        if line is None:
            self.line = []
        else:
            self.line = line
        self.line_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LinesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LinesType.subclass:
            return LinesType.subclass(*args_, **kwargs_)
        else:
            return LinesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_mergedItemIndicator(self):
        return self.mergedItemIndicator
    def set_mergedItemIndicator(self, mergedItemIndicator):
        self.mergedItemIndicator = mergedItemIndicator
    def get_line(self):
        return self.line
    def set_line(self, line):
        self.line = line
    def add_line(self, value):
        self.line.append(value)
    def insert_line_at(self, index, value):
        self.line.insert(index, value)
    def replace_line_at(self, index, value):
        self.line[index] = value
    def _hasContent(self):
        if (
            self.mergedItemIndicator is not None or
            self.line
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LinesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LinesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LinesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LinesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LinesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LinesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='LinesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.mergedItemIndicator is not None:
            namespaceprefix_ = self.mergedItemIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.mergedItemIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smergedItemIndicator>%s</%smergedItemIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.mergedItemIndicator, input_name='mergedItemIndicator'), namespaceprefix_ , eol_))
        for line_ in self.line:
            namespaceprefix_ = self.line_nsprefix_ + ':' if (UseCapturedNS_ and self.line_nsprefix_) else ''
            line_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='line', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='LinesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.mergedItemIndicator is not None:
            mergedItemIndicator_ = self.mergedItemIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}mergedItemIndicator').text = self.gds_format_boolean(mergedItemIndicator_)
        for line_ in self.line:
            line_.to_etree(element, name_='line', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LinesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.mergedItemIndicator is not None:
            showIndent(outfile, level)
            outfile.write('mergedItemIndicator=%s,\n' % self.mergedItemIndicator)
        showIndent(outfile, level)
        outfile.write('line=[\n')
        level += 1
        for line_ in self.line:
            showIndent(outfile, level)
            outfile.write('model_.LineType(\n')
            line_.exportLiteral(outfile, level, name_='LineType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'mergedItemIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'mergedItemIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'mergedItemIndicator')
            self.mergedItemIndicator = ival_
            self.mergedItemIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'line':
            obj_ = LineType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.line.append(obj_)
            obj_.original_tagname_ = 'line'
# end class LinesType


class LineType(GeneratedsSuper):
    """LineType -- A sz
    á
    mla t
    é
    telek (term
    é
    k vagy szolg
    á
    ltat
    á
    s) adatait tartalmaz
    ó
    t
    í
    pus
    Field type including data of invoice items (product or service)
    lineNumber -- A t
    é
    tel sorsz
    á
    ma
    Sequential number of the item
    lineModificationReference -- M
    ó
    dos
    í
    t
    á
    sr
    ó
    l t
    ö
    rt
    é
    n
    ő
    adatszolg
    á
    ltat
    á
    s eset
    é
    n a t
    é
    telsor m
    ó
    dos
    í
    t
    á
    s jelleg
    é
    nek jel
    ö
    l
    é
    se
    Marking the goal of modification of the line (in the case of data supply about changes/updates only)
    referencesToOtherLines -- Hivatkoz
    á
    sok kapcsol
    ó
    d
    ó
    t
    é
    telekre, ha ez az
    Á
    FA t
    ö
    rv
    é
    ny alapj
    á
    n sz
    ü
    ks
    é
    ges
    References to connected items if it is necessary according to VAT law
    advanceData -- El
    ő
    leghez kapcsol
    ó
    d
    ó
    adatok
    Advance related data
    productCodes -- Term
    é
    kk
    ó
    dok
    Product codes
    lineExpressionIndicator -- É
    rt
    é
    ke true, ha a t
    é
    tel mennyis
    é
    gi egys
    é
    ge term
    é
    szetes m
    é
    rt
    é
    kegys
    é
    gben kifejezhet
    ő
    The value is true if the unit of measure of the invoice item is expressible in natural unit
    lineNatureIndicator -- Adott t
    é
    telsor term
    é
    k
    é
    rt
    é
    kes
    í
    t
    é
    s vagy szolg
    á
    ltat
    á
    s ny
    ú
    jt
    á
    s jelleg
    é
    nek jelz
    é
    se
    Indication of the nature of the supply of goods or services on a given line
    lineDescription -- A term
    é
    k vagy szolg
    á
    ltat
    á
    s megnevez
    é
    se
    Name / description of the product or service
    quantity -- Mennyis
    é
    g
    Quantity
    unitOfMeasure -- A sz
    á
    ml
    á
    n szerepl
    ő
    mennyis
    é
    gi egys
    é
    g kanonikus kifejez
    é
    se az interf
    é
    sz specifik
    á
    ci
    ó
    szerint
    Canonical representation of the unit of measure of the invoice, according to the interface specification
    unitOfMeasureOwn -- A sz
    á
    ml
    á
    n szerepl
    ő
    mennyis
    é
    gi egys
    é
    g liter
    á
    lis kifejez
    é
    se
    Literal unit of measure of the invoice
    unitPrice -- Egys
    é
    g
    á
    r a sz
    á
    mla p
    é
    nznem
    é
    ben. Egyszer
    ű
    s
    í
    tett sz
    á
    mla eset
    é
    n brutt
    ó
    , egy
    é
    b esetben nett
    ó
    egys
    é
    g
    á
    r
    Unit price expressed in the currency of the invoice In the event of simplified invoices gross unit price, in other cases net unit price
    unitPriceHUF -- Egys
    é
    g
    á
    r forintban
    Unit price expressed in HUF
    lineDiscountData -- A t
    é
    telhez tartoz
    ó
    á
    rengedm
    é
    ny adatok
    Discount data in relation to the item
    lineAmountsNormal -- Norm
    á
    l (nem egyszer
    ű
    s
    í
    tett) sz
    á
    mla eset
    é
    n (bele
    é
    rtve a gy
    ű
    jt
    ő
    sz
    á
    ml
    á
    t) kit
    ö
    ltend
    ő
    t
    é
    tel
    é
    rt
    é
    k adatok.
    Item value data to be completed in case of normal (not simplified, but including aggregated) invoice
    lineAmountsSimplified -- Egyszer
    ű
    s
    í
    tett sz
    á
    mla eset
    é
    n kit
    ö
    ltend
    ő
    t
    é
    tel
    é
    rt
    é
    k adatok
    Item value data to be completed in case of simplified invoice
    intermediatedService -- É
    rt
    é
    ke true ha a t
    é
    tel k
    ö
    zvet
    í
    tett szolg
    á
    ltat
    á
    s - Sz
    á
    mviteli tv. 3.
    §
    (4) 1
    The value is true if the item is an intermediated service - paragraph (4) 1 of the Article 3 of Accounting Act
    aggregateInvoiceLineData -- Gy
    ű
    jt
    ő
    sz
    á
    mla adatok
    Aggregate invoice data
    newTransportMean -- Ú
    j k
    ö
    zleked
    é
    si eszk
    ö
    z
    é
    rt
    é
    kes
    í
    t
    é
    s
    Á
    FA tv. 89
    §
    ill. 169
    §
    o)
    Supply of new means of transport - section 89
    §
    and 169 (o) of the VAT law
    depositIndicator -- É
    rt
    é
    ke true, ha a t
    é
    tel bet
    é
    td
    í
    j jelleg
    ű
    The value is true if the item is bottle/container deposit
    obligatedForProductFee -- É
    rt
    é
    ke true ha a t
    é
    telt term
    é
    kd
    í
    j fizet
    é
    si k
    ö
    telezetts
    é
    g terheli
    The value is true if the item is liable to product fee
    GPCExcise -- F
    ö
    ldg
    á
    z, villamos energia, sz
    é
    n j
    ö
    ved
    é
    ki ad
    ó
    ja forintban - J
    ö
    t. 118.
    §
    (2)
    Excise duty on natural gas, electricity and coal in Hungarian forints
    –
    paragraph (2), Section 118 of the Act on Excise Duties
    dieselOilPurchase -- G
    á
    zolaj ad
    ó
    zottan t
    ö
    rt
    é
    n
    ő
    beszerz
    é
    s
    é
    nek adatai
    –
    45/2016 (XI. 29.) NGM rendelet 75.
    §
    (1) a)
    Data of gas oil acquisition after taxation
    –
    point a), paragraph (1) of Section 75 of the NGM Decree No. 45/2016. (XI. 29.)
    netaDeclaration -- É
    rt
    é
    ke true, ha a Neta tv-ben meghat
    á
    rozott ad
    ó
    k
    ö
    telezetts
    é
    g az ad
    ó
    alany
    á
    t terheli. 2011.
    é
    vi CIII. tv. 3.
    §
    (2)
    Value is true, if the taxable person is liable for tax obligation determined in the Act on Public Health Product Tax (Neta tv.). Paragraph (2), Section 3 of the Act CIII of 2011
    productFeeClause -- A k
    ö
    rnyezetv
    é
    delmi term
    é
    kd
    í
    jr
    ó
    l sz
    ó
    l
    ó
    2011.
    é
    vi LXXXV. tv. szerinti, t
    é
    telre vonatkoz
    ó
    z
    á
    rad
    é
    kok
    Clauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)
    lineProductFeeContent -- A t
    é
    tel term
    é
    kd
    í
    j tartalm
    á
    ra vonatkoz
    ó
    adatok
    Data on the content of the line's product charge
    conventionalLineInfo -- A sz
    á
    mlafeldolgoz
    á
    st seg
    í
    t
    ő
    , egyezm
    é
    nyesen neves
    í
    tett egy
    é
    b adatok
    Other conventionally named data to assist in invoice processing
    additionalLineData -- A term
    é
    k/szolg
    á
    ltat
    á
    s t
    é
    telhez kapcsol
    ó
    d
    ó
    , tov
    á
    bbi adat
    Other data in relation to the product / service item

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineNumber=None, lineModificationReference=None, referencesToOtherLines=None, advanceData=None, productCodes=None, lineExpressionIndicator=None, lineNatureIndicator=None, lineDescription=None, quantity=None, unitOfMeasure=None, unitOfMeasureOwn=None, unitPrice=None, unitPriceHUF=None, lineDiscountData=None, lineAmountsNormal=None, lineAmountsSimplified=None, intermediatedService=None, aggregateInvoiceLineData=None, newTransportMean=None, depositIndicator=None, obligatedForProductFee=None, GPCExcise=None, dieselOilPurchase=None, netaDeclaration=None, productFeeClause=None, lineProductFeeContent=None, conventionalLineInfo=None, additionalLineData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineNumber = lineNumber
        self.validate_LineNumberType(self.lineNumber)
        self.lineNumber_nsprefix_ = "base"
        self.lineModificationReference = lineModificationReference
        self.lineModificationReference_nsprefix_ = None
        self.referencesToOtherLines = referencesToOtherLines
        self.referencesToOtherLines_nsprefix_ = None
        self.advanceData = advanceData
        self.advanceData_nsprefix_ = None
        self.productCodes = productCodes
        self.productCodes_nsprefix_ = None
        self.lineExpressionIndicator = lineExpressionIndicator
        self.lineExpressionIndicator_nsprefix_ = "xs"
        self.lineNatureIndicator = lineNatureIndicator
        self.validate_LineNatureIndicatorType(self.lineNatureIndicator)
        self.lineNatureIndicator_nsprefix_ = None
        self.lineDescription = lineDescription
        self.validate_SimpleText512NotBlankType(self.lineDescription)
        self.lineDescription_nsprefix_ = "common"
        self.quantity = quantity
        self.validate_QuantityType(self.quantity)
        self.quantity_nsprefix_ = None
        self.unitOfMeasure = unitOfMeasure
        self.validate_UnitOfMeasureType(self.unitOfMeasure)
        self.unitOfMeasure_nsprefix_ = None
        self.unitOfMeasureOwn = unitOfMeasureOwn
        self.validate_SimpleText50NotBlankType(self.unitOfMeasureOwn)
        self.unitOfMeasureOwn_nsprefix_ = "common"
        self.unitPrice = unitPrice
        self.validate_QuantityType(self.unitPrice)
        self.unitPrice_nsprefix_ = None
        self.unitPriceHUF = unitPriceHUF
        self.validate_QuantityType(self.unitPriceHUF)
        self.unitPriceHUF_nsprefix_ = None
        self.lineDiscountData = lineDiscountData
        self.lineDiscountData_nsprefix_ = None
        self.lineAmountsNormal = lineAmountsNormal
        self.lineAmountsNormal_nsprefix_ = None
        self.lineAmountsSimplified = lineAmountsSimplified
        self.lineAmountsSimplified_nsprefix_ = None
        self.intermediatedService = intermediatedService
        self.intermediatedService_nsprefix_ = "xs"
        self.aggregateInvoiceLineData = aggregateInvoiceLineData
        self.aggregateInvoiceLineData_nsprefix_ = None
        self.newTransportMean = newTransportMean
        self.newTransportMean_nsprefix_ = None
        self.depositIndicator = depositIndicator
        self.depositIndicator_nsprefix_ = "xs"
        self.obligatedForProductFee = obligatedForProductFee
        self.obligatedForProductFee_nsprefix_ = "xs"
        self.GPCExcise = GPCExcise
        self.validate_MonetaryType(self.GPCExcise)
        self.GPCExcise_nsprefix_ = "base"
        self.dieselOilPurchase = dieselOilPurchase
        self.dieselOilPurchase_nsprefix_ = None
        self.netaDeclaration = netaDeclaration
        self.netaDeclaration_nsprefix_ = "xs"
        self.productFeeClause = productFeeClause
        self.productFeeClause_nsprefix_ = None
        if lineProductFeeContent is None:
            self.lineProductFeeContent = []
        else:
            self.lineProductFeeContent = lineProductFeeContent
        self.lineProductFeeContent_nsprefix_ = None
        self.conventionalLineInfo = conventionalLineInfo
        self.conventionalLineInfo_nsprefix_ = None
        if additionalLineData is None:
            self.additionalLineData = []
        else:
            self.additionalLineData = additionalLineData
        self.additionalLineData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineType.subclass:
            return LineType.subclass(*args_, **kwargs_)
        else:
            return LineType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineNumber(self):
        return self.lineNumber
    def set_lineNumber(self, lineNumber):
        self.lineNumber = lineNumber
    def get_lineModificationReference(self):
        return self.lineModificationReference
    def set_lineModificationReference(self, lineModificationReference):
        self.lineModificationReference = lineModificationReference
    def get_referencesToOtherLines(self):
        return self.referencesToOtherLines
    def set_referencesToOtherLines(self, referencesToOtherLines):
        self.referencesToOtherLines = referencesToOtherLines
    def get_advanceData(self):
        return self.advanceData
    def set_advanceData(self, advanceData):
        self.advanceData = advanceData
    def get_productCodes(self):
        return self.productCodes
    def set_productCodes(self, productCodes):
        self.productCodes = productCodes
    def get_lineExpressionIndicator(self):
        return self.lineExpressionIndicator
    def set_lineExpressionIndicator(self, lineExpressionIndicator):
        self.lineExpressionIndicator = lineExpressionIndicator
    def get_lineNatureIndicator(self):
        return self.lineNatureIndicator
    def set_lineNatureIndicator(self, lineNatureIndicator):
        self.lineNatureIndicator = lineNatureIndicator
    def get_lineDescription(self):
        return self.lineDescription
    def set_lineDescription(self, lineDescription):
        self.lineDescription = lineDescription
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
    def get_unitOfMeasure(self):
        return self.unitOfMeasure
    def set_unitOfMeasure(self, unitOfMeasure):
        self.unitOfMeasure = unitOfMeasure
    def get_unitOfMeasureOwn(self):
        return self.unitOfMeasureOwn
    def set_unitOfMeasureOwn(self, unitOfMeasureOwn):
        self.unitOfMeasureOwn = unitOfMeasureOwn
    def get_unitPrice(self):
        return self.unitPrice
    def set_unitPrice(self, unitPrice):
        self.unitPrice = unitPrice
    def get_unitPriceHUF(self):
        return self.unitPriceHUF
    def set_unitPriceHUF(self, unitPriceHUF):
        self.unitPriceHUF = unitPriceHUF
    def get_lineDiscountData(self):
        return self.lineDiscountData
    def set_lineDiscountData(self, lineDiscountData):
        self.lineDiscountData = lineDiscountData
    def get_lineAmountsNormal(self):
        return self.lineAmountsNormal
    def set_lineAmountsNormal(self, lineAmountsNormal):
        self.lineAmountsNormal = lineAmountsNormal
    def get_lineAmountsSimplified(self):
        return self.lineAmountsSimplified
    def set_lineAmountsSimplified(self, lineAmountsSimplified):
        self.lineAmountsSimplified = lineAmountsSimplified
    def get_intermediatedService(self):
        return self.intermediatedService
    def set_intermediatedService(self, intermediatedService):
        self.intermediatedService = intermediatedService
    def get_aggregateInvoiceLineData(self):
        return self.aggregateInvoiceLineData
    def set_aggregateInvoiceLineData(self, aggregateInvoiceLineData):
        self.aggregateInvoiceLineData = aggregateInvoiceLineData
    def get_newTransportMean(self):
        return self.newTransportMean
    def set_newTransportMean(self, newTransportMean):
        self.newTransportMean = newTransportMean
    def get_depositIndicator(self):
        return self.depositIndicator
    def set_depositIndicator(self, depositIndicator):
        self.depositIndicator = depositIndicator
    def get_obligatedForProductFee(self):
        return self.obligatedForProductFee
    def set_obligatedForProductFee(self, obligatedForProductFee):
        self.obligatedForProductFee = obligatedForProductFee
    def get_GPCExcise(self):
        return self.GPCExcise
    def set_GPCExcise(self, GPCExcise):
        self.GPCExcise = GPCExcise
    def get_dieselOilPurchase(self):
        return self.dieselOilPurchase
    def set_dieselOilPurchase(self, dieselOilPurchase):
        self.dieselOilPurchase = dieselOilPurchase
    def get_netaDeclaration(self):
        return self.netaDeclaration
    def set_netaDeclaration(self, netaDeclaration):
        self.netaDeclaration = netaDeclaration
    def get_productFeeClause(self):
        return self.productFeeClause
    def set_productFeeClause(self, productFeeClause):
        self.productFeeClause = productFeeClause
    def get_lineProductFeeContent(self):
        return self.lineProductFeeContent
    def set_lineProductFeeContent(self, lineProductFeeContent):
        self.lineProductFeeContent = lineProductFeeContent
    def add_lineProductFeeContent(self, value):
        self.lineProductFeeContent.append(value)
    def insert_lineProductFeeContent_at(self, index, value):
        self.lineProductFeeContent.insert(index, value)
    def replace_lineProductFeeContent_at(self, index, value):
        self.lineProductFeeContent[index] = value
    def get_conventionalLineInfo(self):
        return self.conventionalLineInfo
    def set_conventionalLineInfo(self, conventionalLineInfo):
        self.conventionalLineInfo = conventionalLineInfo
    def get_additionalLineData(self):
        return self.additionalLineData
    def set_additionalLineData(self, additionalLineData):
        self.additionalLineData = additionalLineData
    def add_additionalLineData(self, value):
        self.additionalLineData.append(value)
    def insert_additionalLineData_at(self, index, value):
        self.additionalLineData.insert(index, value)
    def replace_additionalLineData_at(self, index, value):
        self.additionalLineData[index] = value
    def validate_LineNumberType(self, value):
        result = True
        # Validate type LineNumberType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_LineNatureIndicatorType(self, value):
        result = True
        # Validate type LineNatureIndicatorType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['PRODUCT', 'SERVICE', 'OTHER']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LineNatureIndicatorType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LineNatureIndicatorType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LineNatureIndicatorType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_SimpleText512NotBlankType(self, value):
        result = True
        # Validate type SimpleText512NotBlankType, a restriction on AtomicStringType512.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText512NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText512NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText512NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText512NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText512NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_UnitOfMeasureType(self, value):
        result = True
        # Validate type UnitOfMeasureType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['PIECE', 'KILOGRAM', 'TON', 'KWH', 'DAY', 'HOUR', 'MINUTE', 'MONTH', 'LITER', 'KILOMETER', 'CUBIC_METER', 'METER', 'LINEAR_METER', 'CARTON', 'PACK', 'OWN']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on UnitOfMeasureType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on UnitOfMeasureType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on UnitOfMeasureType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.lineNumber is not None or
            self.lineModificationReference is not None or
            self.referencesToOtherLines is not None or
            self.advanceData is not None or
            self.productCodes is not None or
            self.lineExpressionIndicator is not None or
            self.lineNatureIndicator is not None or
            self.lineDescription is not None or
            self.quantity is not None or
            self.unitOfMeasure is not None or
            self.unitOfMeasureOwn is not None or
            self.unitPrice is not None or
            self.unitPriceHUF is not None or
            self.lineDiscountData is not None or
            self.lineAmountsNormal is not None or
            self.lineAmountsSimplified is not None or
            self.intermediatedService is not None or
            self.aggregateInvoiceLineData is not None or
            self.newTransportMean is not None or
            self.depositIndicator is not None or
            self.obligatedForProductFee is not None or
            self.GPCExcise is not None or
            self.dieselOilPurchase is not None or
            self.netaDeclaration is not None or
            self.productFeeClause is not None or
            self.lineProductFeeContent or
            self.conventionalLineInfo is not None or
            self.additionalLineData
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='LineType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='LineType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineNumber is not None:
            namespaceprefix_ = self.lineNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNumber>%s</%slineNumber>%s' % (namespaceprefix_ , self.gds_format_integer(self.lineNumber, input_name='lineNumber'), namespaceprefix_ , eol_))
        if self.lineModificationReference is not None:
            namespaceprefix_ = self.lineModificationReference_nsprefix_ + ':' if (UseCapturedNS_ and self.lineModificationReference_nsprefix_) else ''
            self.lineModificationReference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineModificationReference', pretty_print=pretty_print)
        if self.referencesToOtherLines is not None:
            namespaceprefix_ = self.referencesToOtherLines_nsprefix_ + ':' if (UseCapturedNS_ and self.referencesToOtherLines_nsprefix_) else ''
            self.referencesToOtherLines.export(outfile, level, namespaceprefix_, namespacedef_='', name_='referencesToOtherLines', pretty_print=pretty_print)
        if self.advanceData is not None:
            namespaceprefix_ = self.advanceData_nsprefix_ + ':' if (UseCapturedNS_ and self.advanceData_nsprefix_) else ''
            self.advanceData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='advanceData', pretty_print=pretty_print)
        if self.productCodes is not None:
            namespaceprefix_ = self.productCodes_nsprefix_ + ':' if (UseCapturedNS_ and self.productCodes_nsprefix_) else ''
            self.productCodes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productCodes', pretty_print=pretty_print)
        if self.lineExpressionIndicator is not None:
            namespaceprefix_ = self.lineExpressionIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.lineExpressionIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineExpressionIndicator>%s</%slineExpressionIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.lineExpressionIndicator, input_name='lineExpressionIndicator'), namespaceprefix_ , eol_))
        if self.lineNatureIndicator is not None:
            namespaceprefix_ = self.lineNatureIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.lineNatureIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineNatureIndicator>%s</%slineNatureIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lineNatureIndicator), input_name='lineNatureIndicator')), namespaceprefix_ , eol_))
        if self.lineDescription is not None:
            namespaceprefix_ = self.lineDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.lineDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineDescription>%s</%slineDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lineDescription), input_name='lineDescription')), namespaceprefix_ , eol_))
        if self.quantity is not None:
            namespaceprefix_ = self.quantity_nsprefix_ + ':' if (UseCapturedNS_ and self.quantity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squantity>%s</%squantity>%s' % (namespaceprefix_ , self.gds_format_decimal(self.quantity, input_name='quantity'), namespaceprefix_ , eol_))
        if self.unitOfMeasure is not None:
            namespaceprefix_ = self.unitOfMeasure_nsprefix_ + ':' if (UseCapturedNS_ and self.unitOfMeasure_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitOfMeasure>%s</%sunitOfMeasure>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unitOfMeasure), input_name='unitOfMeasure')), namespaceprefix_ , eol_))
        if self.unitOfMeasureOwn is not None:
            namespaceprefix_ = self.unitOfMeasureOwn_nsprefix_ + ':' if (UseCapturedNS_ and self.unitOfMeasureOwn_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitOfMeasureOwn>%s</%sunitOfMeasureOwn>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unitOfMeasureOwn), input_name='unitOfMeasureOwn')), namespaceprefix_ , eol_))
        if self.unitPrice is not None:
            namespaceprefix_ = self.unitPrice_nsprefix_ + ':' if (UseCapturedNS_ and self.unitPrice_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitPrice>%s</%sunitPrice>%s' % (namespaceprefix_ , self.gds_format_decimal(self.unitPrice, input_name='unitPrice'), namespaceprefix_ , eol_))
        if self.unitPriceHUF is not None:
            namespaceprefix_ = self.unitPriceHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.unitPriceHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitPriceHUF>%s</%sunitPriceHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.unitPriceHUF, input_name='unitPriceHUF'), namespaceprefix_ , eol_))
        if self.lineDiscountData is not None:
            namespaceprefix_ = self.lineDiscountData_nsprefix_ + ':' if (UseCapturedNS_ and self.lineDiscountData_nsprefix_) else ''
            self.lineDiscountData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineDiscountData', pretty_print=pretty_print)
        if self.lineAmountsNormal is not None:
            namespaceprefix_ = self.lineAmountsNormal_nsprefix_ + ':' if (UseCapturedNS_ and self.lineAmountsNormal_nsprefix_) else ''
            self.lineAmountsNormal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineAmountsNormal', pretty_print=pretty_print)
        if self.lineAmountsSimplified is not None:
            namespaceprefix_ = self.lineAmountsSimplified_nsprefix_ + ':' if (UseCapturedNS_ and self.lineAmountsSimplified_nsprefix_) else ''
            self.lineAmountsSimplified.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineAmountsSimplified', pretty_print=pretty_print)
        if self.intermediatedService is not None:
            namespaceprefix_ = self.intermediatedService_nsprefix_ + ':' if (UseCapturedNS_ and self.intermediatedService_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sintermediatedService>%s</%sintermediatedService>%s' % (namespaceprefix_ , self.gds_format_boolean(self.intermediatedService, input_name='intermediatedService'), namespaceprefix_ , eol_))
        if self.aggregateInvoiceLineData is not None:
            namespaceprefix_ = self.aggregateInvoiceLineData_nsprefix_ + ':' if (UseCapturedNS_ and self.aggregateInvoiceLineData_nsprefix_) else ''
            self.aggregateInvoiceLineData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='aggregateInvoiceLineData', pretty_print=pretty_print)
        if self.newTransportMean is not None:
            namespaceprefix_ = self.newTransportMean_nsprefix_ + ':' if (UseCapturedNS_ and self.newTransportMean_nsprefix_) else ''
            self.newTransportMean.export(outfile, level, namespaceprefix_, namespacedef_='', name_='newTransportMean', pretty_print=pretty_print)
        if self.depositIndicator is not None:
            namespaceprefix_ = self.depositIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.depositIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdepositIndicator>%s</%sdepositIndicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.depositIndicator, input_name='depositIndicator'), namespaceprefix_ , eol_))
        if self.obligatedForProductFee is not None:
            namespaceprefix_ = self.obligatedForProductFee_nsprefix_ + ':' if (UseCapturedNS_ and self.obligatedForProductFee_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sobligatedForProductFee>%s</%sobligatedForProductFee>%s' % (namespaceprefix_ , self.gds_format_boolean(self.obligatedForProductFee, input_name='obligatedForProductFee'), namespaceprefix_ , eol_))
        if self.GPCExcise is not None:
            namespaceprefix_ = self.GPCExcise_nsprefix_ + ':' if (UseCapturedNS_ and self.GPCExcise_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sGPCExcise>%s</%sGPCExcise>%s' % (namespaceprefix_ , self.gds_format_decimal(self.GPCExcise, input_name='GPCExcise'), namespaceprefix_ , eol_))
        if self.dieselOilPurchase is not None:
            namespaceprefix_ = self.dieselOilPurchase_nsprefix_ + ':' if (UseCapturedNS_ and self.dieselOilPurchase_nsprefix_) else ''
            self.dieselOilPurchase.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dieselOilPurchase', pretty_print=pretty_print)
        if self.netaDeclaration is not None:
            namespaceprefix_ = self.netaDeclaration_nsprefix_ + ':' if (UseCapturedNS_ and self.netaDeclaration_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snetaDeclaration>%s</%snetaDeclaration>%s' % (namespaceprefix_ , self.gds_format_boolean(self.netaDeclaration, input_name='netaDeclaration'), namespaceprefix_ , eol_))
        if self.productFeeClause is not None:
            namespaceprefix_ = self.productFeeClause_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeClause_nsprefix_) else ''
            self.productFeeClause.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productFeeClause', pretty_print=pretty_print)
        for lineProductFeeContent_ in self.lineProductFeeContent:
            namespaceprefix_ = self.lineProductFeeContent_nsprefix_ + ':' if (UseCapturedNS_ and self.lineProductFeeContent_nsprefix_) else ''
            lineProductFeeContent_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lineProductFeeContent', pretty_print=pretty_print)
        if self.conventionalLineInfo is not None:
            namespaceprefix_ = self.conventionalLineInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.conventionalLineInfo_nsprefix_) else ''
            self.conventionalLineInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='conventionalLineInfo', pretty_print=pretty_print)
        for additionalLineData_ in self.additionalLineData:
            namespaceprefix_ = self.additionalLineData_nsprefix_ + ':' if (UseCapturedNS_ and self.additionalLineData_nsprefix_) else ''
            additionalLineData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='additionalLineData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='LineType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineNumber is not None:
            lineNumber_ = self.lineNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineNumber').text = self.gds_format_integer(lineNumber_)
        if self.lineModificationReference is not None:
            lineModificationReference_ = self.lineModificationReference
            lineModificationReference_.to_etree(element, name_='lineModificationReference', mapping_=mapping_, nsmap_=nsmap_)
        if self.referencesToOtherLines is not None:
            referencesToOtherLines_ = self.referencesToOtherLines
            referencesToOtherLines_.to_etree(element, name_='referencesToOtherLines', mapping_=mapping_, nsmap_=nsmap_)
        if self.advanceData is not None:
            advanceData_ = self.advanceData
            advanceData_.to_etree(element, name_='advanceData', mapping_=mapping_, nsmap_=nsmap_)
        if self.productCodes is not None:
            productCodes_ = self.productCodes
            productCodes_.to_etree(element, name_='productCodes', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineExpressionIndicator is not None:
            lineExpressionIndicator_ = self.lineExpressionIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineExpressionIndicator').text = self.gds_format_boolean(lineExpressionIndicator_)
        if self.lineNatureIndicator is not None:
            lineNatureIndicator_ = self.lineNatureIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineNatureIndicator').text = self.gds_format_string(lineNatureIndicator_)
        if self.lineDescription is not None:
            lineDescription_ = self.lineDescription
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineDescription').text = self.gds_format_string(lineDescription_)
        if self.quantity is not None:
            quantity_ = self.quantity
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}quantity').text = self.gds_format_decimal(quantity_)
        if self.unitOfMeasure is not None:
            unitOfMeasure_ = self.unitOfMeasure
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}unitOfMeasure').text = self.gds_format_string(unitOfMeasure_)
        if self.unitOfMeasureOwn is not None:
            unitOfMeasureOwn_ = self.unitOfMeasureOwn
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}unitOfMeasureOwn').text = self.gds_format_string(unitOfMeasureOwn_)
        if self.unitPrice is not None:
            unitPrice_ = self.unitPrice
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}unitPrice').text = self.gds_format_decimal(unitPrice_)
        if self.unitPriceHUF is not None:
            unitPriceHUF_ = self.unitPriceHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}unitPriceHUF').text = self.gds_format_decimal(unitPriceHUF_)
        if self.lineDiscountData is not None:
            lineDiscountData_ = self.lineDiscountData
            lineDiscountData_.to_etree(element, name_='lineDiscountData', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineAmountsNormal is not None:
            lineAmountsNormal_ = self.lineAmountsNormal
            lineAmountsNormal_.to_etree(element, name_='lineAmountsNormal', mapping_=mapping_, nsmap_=nsmap_)
        if self.lineAmountsSimplified is not None:
            lineAmountsSimplified_ = self.lineAmountsSimplified
            lineAmountsSimplified_.to_etree(element, name_='lineAmountsSimplified', mapping_=mapping_, nsmap_=nsmap_)
        if self.intermediatedService is not None:
            intermediatedService_ = self.intermediatedService
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}intermediatedService').text = self.gds_format_boolean(intermediatedService_)
        if self.aggregateInvoiceLineData is not None:
            aggregateInvoiceLineData_ = self.aggregateInvoiceLineData
            aggregateInvoiceLineData_.to_etree(element, name_='aggregateInvoiceLineData', mapping_=mapping_, nsmap_=nsmap_)
        if self.newTransportMean is not None:
            newTransportMean_ = self.newTransportMean
            newTransportMean_.to_etree(element, name_='newTransportMean', mapping_=mapping_, nsmap_=nsmap_)
        if self.depositIndicator is not None:
            depositIndicator_ = self.depositIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}depositIndicator').text = self.gds_format_boolean(depositIndicator_)
        if self.obligatedForProductFee is not None:
            obligatedForProductFee_ = self.obligatedForProductFee
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}obligatedForProductFee').text = self.gds_format_boolean(obligatedForProductFee_)
        if self.GPCExcise is not None:
            GPCExcise_ = self.GPCExcise
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}GPCExcise').text = self.gds_format_decimal(GPCExcise_)
        if self.dieselOilPurchase is not None:
            dieselOilPurchase_ = self.dieselOilPurchase
            dieselOilPurchase_.to_etree(element, name_='dieselOilPurchase', mapping_=mapping_, nsmap_=nsmap_)
        if self.netaDeclaration is not None:
            netaDeclaration_ = self.netaDeclaration
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}netaDeclaration').text = self.gds_format_boolean(netaDeclaration_)
        if self.productFeeClause is not None:
            productFeeClause_ = self.productFeeClause
            productFeeClause_.to_etree(element, name_='productFeeClause', mapping_=mapping_, nsmap_=nsmap_)
        for lineProductFeeContent_ in self.lineProductFeeContent:
            lineProductFeeContent_.to_etree(element, name_='lineProductFeeContent', mapping_=mapping_, nsmap_=nsmap_)
        if self.conventionalLineInfo is not None:
            conventionalLineInfo_ = self.conventionalLineInfo
            conventionalLineInfo_.to_etree(element, name_='conventionalLineInfo', mapping_=mapping_, nsmap_=nsmap_)
        for additionalLineData_ in self.additionalLineData:
            additionalLineData_.to_etree(element, name_='additionalLineData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineNumber is not None:
            showIndent(outfile, level)
            outfile.write('lineNumber=%d,\n' % self.lineNumber)
        if self.lineModificationReference is not None:
            showIndent(outfile, level)
            outfile.write('lineModificationReference=model_.LineModificationReferenceType(\n')
            self.lineModificationReference.exportLiteral(outfile, level, name_='lineModificationReference')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.referencesToOtherLines is not None:
            showIndent(outfile, level)
            outfile.write('referencesToOtherLines=model_.ReferencesToOtherLinesType(\n')
            self.referencesToOtherLines.exportLiteral(outfile, level, name_='referencesToOtherLines')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.advanceData is not None:
            showIndent(outfile, level)
            outfile.write('advanceData=model_.AdvanceDataType(\n')
            self.advanceData.exportLiteral(outfile, level, name_='advanceData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.productCodes is not None:
            showIndent(outfile, level)
            outfile.write('productCodes=model_.ProductCodesType(\n')
            self.productCodes.exportLiteral(outfile, level, name_='productCodes')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineExpressionIndicator is not None:
            showIndent(outfile, level)
            outfile.write('lineExpressionIndicator=%s,\n' % self.lineExpressionIndicator)
        if self.lineNatureIndicator is not None:
            showIndent(outfile, level)
            outfile.write('lineNatureIndicator=%s,\n' % self.gds_encode(quote_python(self.lineNatureIndicator)))
        if self.lineDescription is not None:
            showIndent(outfile, level)
            outfile.write('lineDescription=%s,\n' % self.gds_encode(quote_python(self.lineDescription)))
        if self.quantity is not None:
            showIndent(outfile, level)
            outfile.write('quantity=%f,\n' % self.quantity)
        if self.unitOfMeasure is not None:
            showIndent(outfile, level)
            outfile.write('unitOfMeasure=%s,\n' % self.gds_encode(quote_python(self.unitOfMeasure)))
        if self.unitOfMeasureOwn is not None:
            showIndent(outfile, level)
            outfile.write('unitOfMeasureOwn=%s,\n' % self.gds_encode(quote_python(self.unitOfMeasureOwn)))
        if self.unitPrice is not None:
            showIndent(outfile, level)
            outfile.write('unitPrice=%f,\n' % self.unitPrice)
        if self.unitPriceHUF is not None:
            showIndent(outfile, level)
            outfile.write('unitPriceHUF=%f,\n' % self.unitPriceHUF)
        if self.lineDiscountData is not None:
            showIndent(outfile, level)
            outfile.write('lineDiscountData=model_.DiscountDataType(\n')
            self.lineDiscountData.exportLiteral(outfile, level, name_='lineDiscountData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineAmountsNormal is not None:
            showIndent(outfile, level)
            outfile.write('lineAmountsNormal=model_.LineAmountsNormalType(\n')
            self.lineAmountsNormal.exportLiteral(outfile, level, name_='lineAmountsNormal')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.lineAmountsSimplified is not None:
            showIndent(outfile, level)
            outfile.write('lineAmountsSimplified=model_.LineAmountsSimplifiedType(\n')
            self.lineAmountsSimplified.exportLiteral(outfile, level, name_='lineAmountsSimplified')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.intermediatedService is not None:
            showIndent(outfile, level)
            outfile.write('intermediatedService=%s,\n' % self.intermediatedService)
        if self.aggregateInvoiceLineData is not None:
            showIndent(outfile, level)
            outfile.write('aggregateInvoiceLineData=model_.AggregateInvoiceLineDataType(\n')
            self.aggregateInvoiceLineData.exportLiteral(outfile, level, name_='aggregateInvoiceLineData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.newTransportMean is not None:
            showIndent(outfile, level)
            outfile.write('newTransportMean=model_.NewTransportMeanType(\n')
            self.newTransportMean.exportLiteral(outfile, level, name_='newTransportMean')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.depositIndicator is not None:
            showIndent(outfile, level)
            outfile.write('depositIndicator=%s,\n' % self.depositIndicator)
        if self.obligatedForProductFee is not None:
            showIndent(outfile, level)
            outfile.write('obligatedForProductFee=%s,\n' % self.obligatedForProductFee)
        if self.GPCExcise is not None:
            showIndent(outfile, level)
            outfile.write('GPCExcise=%f,\n' % self.GPCExcise)
        if self.dieselOilPurchase is not None:
            showIndent(outfile, level)
            outfile.write('dieselOilPurchase=model_.DieselOilPurchaseType(\n')
            self.dieselOilPurchase.exportLiteral(outfile, level, name_='dieselOilPurchase')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.netaDeclaration is not None:
            showIndent(outfile, level)
            outfile.write('netaDeclaration=%s,\n' % self.netaDeclaration)
        if self.productFeeClause is not None:
            showIndent(outfile, level)
            outfile.write('productFeeClause=model_.ProductFeeClauseType(\n')
            self.productFeeClause.exportLiteral(outfile, level, name_='productFeeClause')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('lineProductFeeContent=[\n')
        level += 1
        for lineProductFeeContent_ in self.lineProductFeeContent:
            showIndent(outfile, level)
            outfile.write('model_.ProductFeeDataType(\n')
            lineProductFeeContent_.exportLiteral(outfile, level, name_='ProductFeeDataType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.conventionalLineInfo is not None:
            showIndent(outfile, level)
            outfile.write('conventionalLineInfo=model_.ConventionalInvoiceInfoType(\n')
            self.conventionalLineInfo.exportLiteral(outfile, level, name_='conventionalLineInfo')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('additionalLineData=[\n')
        level += 1
        for additionalLineData_ in self.additionalLineData:
            showIndent(outfile, level)
            outfile.write('model_.AdditionalDataType(\n')
            additionalLineData_.exportLiteral(outfile, level, name_='AdditionalDataType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'lineNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'lineNumber')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'lineNumber')
            self.lineNumber = ival_
            self.lineNumber_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.lineNumber)
        elif nodeName_ == 'lineModificationReference':
            obj_ = LineModificationReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineModificationReference = obj_
            obj_.original_tagname_ = 'lineModificationReference'
        elif nodeName_ == 'referencesToOtherLines':
            obj_ = ReferencesToOtherLinesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.referencesToOtherLines = obj_
            obj_.original_tagname_ = 'referencesToOtherLines'
        elif nodeName_ == 'advanceData':
            obj_ = AdvanceDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.advanceData = obj_
            obj_.original_tagname_ = 'advanceData'
        elif nodeName_ == 'productCodes':
            obj_ = ProductCodesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productCodes = obj_
            obj_.original_tagname_ = 'productCodes'
        elif nodeName_ == 'lineExpressionIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'lineExpressionIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'lineExpressionIndicator')
            self.lineExpressionIndicator = ival_
            self.lineExpressionIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'lineNatureIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lineNatureIndicator')
            value_ = self.gds_validate_string(value_, node, 'lineNatureIndicator')
            self.lineNatureIndicator = value_
            self.lineNatureIndicator_nsprefix_ = child_.prefix
            # validate type LineNatureIndicatorType
            self.validate_LineNatureIndicatorType(self.lineNatureIndicator)
        elif nodeName_ == 'lineDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lineDescription')
            value_ = self.gds_validate_string(value_, node, 'lineDescription')
            self.lineDescription = value_
            self.lineDescription_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.lineDescription)
        elif nodeName_ == 'quantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'quantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'quantity')
            self.quantity = fval_
            self.quantity_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.quantity)
        elif nodeName_ == 'unitOfMeasure':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unitOfMeasure')
            value_ = self.gds_validate_string(value_, node, 'unitOfMeasure')
            self.unitOfMeasure = value_
            self.unitOfMeasure_nsprefix_ = child_.prefix
            # validate type UnitOfMeasureType
            self.validate_UnitOfMeasureType(self.unitOfMeasure)
        elif nodeName_ == 'unitOfMeasureOwn':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unitOfMeasureOwn')
            value_ = self.gds_validate_string(value_, node, 'unitOfMeasureOwn')
            self.unitOfMeasureOwn = value_
            self.unitOfMeasureOwn_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.unitOfMeasureOwn)
        elif nodeName_ == 'unitPrice' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'unitPrice')
            fval_ = self.gds_validate_decimal(fval_, node, 'unitPrice')
            self.unitPrice = fval_
            self.unitPrice_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.unitPrice)
        elif nodeName_ == 'unitPriceHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'unitPriceHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'unitPriceHUF')
            self.unitPriceHUF = fval_
            self.unitPriceHUF_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.unitPriceHUF)
        elif nodeName_ == 'lineDiscountData':
            obj_ = DiscountDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineDiscountData = obj_
            obj_.original_tagname_ = 'lineDiscountData'
        elif nodeName_ == 'lineAmountsNormal':
            obj_ = LineAmountsNormalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineAmountsNormal = obj_
            obj_.original_tagname_ = 'lineAmountsNormal'
        elif nodeName_ == 'lineAmountsSimplified':
            obj_ = LineAmountsSimplifiedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineAmountsSimplified = obj_
            obj_.original_tagname_ = 'lineAmountsSimplified'
        elif nodeName_ == 'intermediatedService':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'intermediatedService')
            ival_ = self.gds_validate_boolean(ival_, node, 'intermediatedService')
            self.intermediatedService = ival_
            self.intermediatedService_nsprefix_ = child_.prefix
        elif nodeName_ == 'aggregateInvoiceLineData':
            obj_ = AggregateInvoiceLineDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.aggregateInvoiceLineData = obj_
            obj_.original_tagname_ = 'aggregateInvoiceLineData'
        elif nodeName_ == 'newTransportMean':
            obj_ = NewTransportMeanType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.newTransportMean = obj_
            obj_.original_tagname_ = 'newTransportMean'
        elif nodeName_ == 'depositIndicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'depositIndicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'depositIndicator')
            self.depositIndicator = ival_
            self.depositIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'obligatedForProductFee':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'obligatedForProductFee')
            ival_ = self.gds_validate_boolean(ival_, node, 'obligatedForProductFee')
            self.obligatedForProductFee = ival_
            self.obligatedForProductFee_nsprefix_ = child_.prefix
        elif nodeName_ == 'GPCExcise' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'GPCExcise')
            fval_ = self.gds_validate_decimal(fval_, node, 'GPCExcise')
            self.GPCExcise = fval_
            self.GPCExcise_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.GPCExcise)
        elif nodeName_ == 'dieselOilPurchase':
            obj_ = DieselOilPurchaseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dieselOilPurchase = obj_
            obj_.original_tagname_ = 'dieselOilPurchase'
        elif nodeName_ == 'netaDeclaration':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'netaDeclaration')
            ival_ = self.gds_validate_boolean(ival_, node, 'netaDeclaration')
            self.netaDeclaration = ival_
            self.netaDeclaration_nsprefix_ = child_.prefix
        elif nodeName_ == 'productFeeClause':
            obj_ = ProductFeeClauseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productFeeClause = obj_
            obj_.original_tagname_ = 'productFeeClause'
        elif nodeName_ == 'lineProductFeeContent':
            obj_ = ProductFeeDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lineProductFeeContent.append(obj_)
            obj_.original_tagname_ = 'lineProductFeeContent'
        elif nodeName_ == 'conventionalLineInfo':
            obj_ = ConventionalInvoiceInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.conventionalLineInfo = obj_
            obj_.original_tagname_ = 'conventionalLineInfo'
        elif nodeName_ == 'additionalLineData':
            obj_ = AdditionalDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.additionalLineData.append(obj_)
            obj_.original_tagname_ = 'additionalLineData'
# end class LineType


class LineVatDataType(GeneratedsSuper):
    """LineVatDataType -- T
    é
    tel
    Á
    FA adatok
    Line VAT data
    lineVatAmount -- T
    é
    tel
    Á
    FA
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben
    VAT amount of the item expressed in the currency of the invoice
    lineVatAmountHUF -- T
    é
    tel
    Á
    FA
    ö
    sszege forintban
    VAT amount of the item expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lineVatAmount=None, lineVatAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lineVatAmount = lineVatAmount
        self.validate_MonetaryType(self.lineVatAmount)
        self.lineVatAmount_nsprefix_ = "base"
        self.lineVatAmountHUF = lineVatAmountHUF
        self.validate_MonetaryType(self.lineVatAmountHUF)
        self.lineVatAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineVatDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineVatDataType.subclass:
            return LineVatDataType.subclass(*args_, **kwargs_)
        else:
            return LineVatDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lineVatAmount(self):
        return self.lineVatAmount
    def set_lineVatAmount(self, lineVatAmount):
        self.lineVatAmount = lineVatAmount
    def get_lineVatAmountHUF(self):
        return self.lineVatAmountHUF
    def set_lineVatAmountHUF(self, lineVatAmountHUF):
        self.lineVatAmountHUF = lineVatAmountHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.lineVatAmount is not None or
            self.lineVatAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineVatDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineVatDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineVatDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineVatDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineVatDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineVatDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='LineVatDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lineVatAmount is not None:
            namespaceprefix_ = self.lineVatAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineVatAmount>%s</%slineVatAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineVatAmount, input_name='lineVatAmount'), namespaceprefix_ , eol_))
        if self.lineVatAmountHUF is not None:
            namespaceprefix_ = self.lineVatAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.lineVatAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slineVatAmountHUF>%s</%slineVatAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.lineVatAmountHUF, input_name='lineVatAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='LineVatDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.lineVatAmount is not None:
            lineVatAmount_ = self.lineVatAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineVatAmount').text = self.gds_format_decimal(lineVatAmount_)
        if self.lineVatAmountHUF is not None:
            lineVatAmountHUF_ = self.lineVatAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}lineVatAmountHUF').text = self.gds_format_decimal(lineVatAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='LineVatDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.lineVatAmount is not None:
            showIndent(outfile, level)
            outfile.write('lineVatAmount=%f,\n' % self.lineVatAmount)
        if self.lineVatAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('lineVatAmountHUF=%f,\n' % self.lineVatAmountHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'lineVatAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineVatAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineVatAmount')
            self.lineVatAmount = fval_
            self.lineVatAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineVatAmount)
        elif nodeName_ == 'lineVatAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'lineVatAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'lineVatAmountHUF')
            self.lineVatAmountHUF = fval_
            self.lineVatAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.lineVatAmountHUF)
# end class LineVatDataType


class MaterialNumbersType(GeneratedsSuper):
    """MaterialNumbersType -- Anyagsz
    á
    mok
    Material numbers
    materialNumber -- Anyagsz
    á
    m
    Material number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, materialNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if materialNumber is None:
            self.materialNumber = []
        else:
            self.materialNumber = materialNumber
        self.materialNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MaterialNumbersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MaterialNumbersType.subclass:
            return MaterialNumbersType.subclass(*args_, **kwargs_)
        else:
            return MaterialNumbersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_materialNumber(self):
        return self.materialNumber
    def set_materialNumber(self, materialNumber):
        self.materialNumber = materialNumber
    def add_materialNumber(self, value):
        self.materialNumber.append(value)
    def insert_materialNumber_at(self, index, value):
        self.materialNumber.insert(index, value)
    def replace_materialNumber_at(self, index, value):
        self.materialNumber[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.materialNumber
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='MaterialNumbersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MaterialNumbersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MaterialNumbersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MaterialNumbersType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MaterialNumbersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MaterialNumbersType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='MaterialNumbersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for materialNumber_ in self.materialNumber:
            namespaceprefix_ = self.materialNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.materialNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smaterialNumber>%s</%smaterialNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(materialNumber_), input_name='materialNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='MaterialNumbersType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for materialNumber_ in self.materialNumber:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}materialNumber').text = self.gds_format_string(materialNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MaterialNumbersType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('materialNumber=[\n')
        level += 1
        for materialNumber_ in self.materialNumber:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(materialNumber_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'materialNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'materialNumber')
            value_ = self.gds_validate_string(value_, node, 'materialNumber')
            self.materialNumber.append(value_)
            self.materialNumber_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.materialNumber[-1])
# end class MaterialNumbersType


class NewTransportMeanType(GeneratedsSuper):
    """NewTransportMeanType -- Ú
    j k
    ö
    zleked
    é
    si eszk
    ö
    z
    é
    rt
    é
    kes
    í
    t
    é
    s
    Á
    FA tv. 89
    §
    ill. 169
    §
    o)
    Supply of new means of transport - section 89
    §
    and 169 (o) of the VAT law
    brand -- Gy
    á
    rtm
    á
    ny/t
    í
    pus
    Product / type
    serialNum -- Alv
    á
    zsz
    á
    m/gy
    á
    ri sz
    á
    m/Gy
    á
    rt
    á
    si sz
    á
    m
    Chassis number / serial number / product number
    engineNum -- Motorsz
    á
    m
    Engine number
    firstEntryIntoService -- Els
    ő
    forgalomba helyez
    é
    s id
    ő
    pontja
    First entry into service
    vehicle -- Sz
    á
    razf
    ö
    ldi k
    ö
    zleked
    é
    si eszk
    ö
    z tov
    á
    bbi adatai
    Other data in relation to motorised land vehicle
    vessel -- V
    í
    zi j
    á
    rm
    ű
    adatai
    Data of vessel
    aircraft -- L
    é
    gi k
    ö
    zleked
    é
    si eszk
    ö
    z
    Aircraft

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, brand=None, serialNum=None, engineNum=None, firstEntryIntoService=None, vehicle=None, vessel=None, aircraft=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.brand = brand
        self.validate_SimpleText50NotBlankType(self.brand)
        self.brand_nsprefix_ = "common"
        self.serialNum = serialNum
        self.validate_SimpleText255NotBlankType(self.serialNum)
        self.serialNum_nsprefix_ = "common"
        self.engineNum = engineNum
        self.validate_SimpleText255NotBlankType(self.engineNum)
        self.engineNum_nsprefix_ = "common"
        if isinstance(firstEntryIntoService, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(firstEntryIntoService, '%Y-%m-%d').date()
        else:
            initvalue_ = firstEntryIntoService
        self.firstEntryIntoService = initvalue_
        self.firstEntryIntoService_nsprefix_ = "base"
        self.vehicle = vehicle
        self.vehicle_nsprefix_ = None
        self.vessel = vessel
        self.vessel_nsprefix_ = None
        self.aircraft = aircraft
        self.aircraft_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NewTransportMeanType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NewTransportMeanType.subclass:
            return NewTransportMeanType.subclass(*args_, **kwargs_)
        else:
            return NewTransportMeanType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_brand(self):
        return self.brand
    def set_brand(self, brand):
        self.brand = brand
    def get_serialNum(self):
        return self.serialNum
    def set_serialNum(self, serialNum):
        self.serialNum = serialNum
    def get_engineNum(self):
        return self.engineNum
    def set_engineNum(self, engineNum):
        self.engineNum = engineNum
    def get_firstEntryIntoService(self):
        return self.firstEntryIntoService
    def set_firstEntryIntoService(self, firstEntryIntoService):
        self.firstEntryIntoService = firstEntryIntoService
    def get_vehicle(self):
        return self.vehicle
    def set_vehicle(self, vehicle):
        self.vehicle = vehicle
    def get_vessel(self):
        return self.vessel
    def set_vessel(self, vessel):
        self.vessel = vessel
    def get_aircraft(self):
        return self.aircraft
    def set_aircraft(self, aircraft):
        self.aircraft = aircraft
    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_SimpleText255NotBlankType(self, value):
        result = True
        # Validate type SimpleText255NotBlankType, a restriction on AtomicStringType255.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText255NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText255NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText255NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText255NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText255NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceDateType_patterns_, ))
                result = False
        return result
    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]
    def _hasContent(self):
        if (
            self.brand is not None or
            self.serialNum is not None or
            self.engineNum is not None or
            self.firstEntryIntoService is not None or
            self.vehicle is not None or
            self.vessel is not None or
            self.aircraft is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='NewTransportMeanType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NewTransportMeanType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NewTransportMeanType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NewTransportMeanType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NewTransportMeanType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NewTransportMeanType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='NewTransportMeanType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.brand is not None:
            namespaceprefix_ = self.brand_nsprefix_ + ':' if (UseCapturedNS_ and self.brand_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbrand>%s</%sbrand>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.brand), input_name='brand')), namespaceprefix_ , eol_))
        if self.serialNum is not None:
            namespaceprefix_ = self.serialNum_nsprefix_ + ':' if (UseCapturedNS_ and self.serialNum_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sserialNum>%s</%sserialNum>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.serialNum), input_name='serialNum')), namespaceprefix_ , eol_))
        if self.engineNum is not None:
            namespaceprefix_ = self.engineNum_nsprefix_ + ':' if (UseCapturedNS_ and self.engineNum_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sengineNum>%s</%sengineNum>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.engineNum), input_name='engineNum')), namespaceprefix_ , eol_))
        if self.firstEntryIntoService is not None:
            namespaceprefix_ = self.firstEntryIntoService_nsprefix_ + ':' if (UseCapturedNS_ and self.firstEntryIntoService_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstEntryIntoService>%s</%sfirstEntryIntoService>%s' % (namespaceprefix_ , self.gds_format_date(self.firstEntryIntoService, input_name='firstEntryIntoService'), namespaceprefix_ , eol_))
        if self.vehicle is not None:
            namespaceprefix_ = self.vehicle_nsprefix_ + ':' if (UseCapturedNS_ and self.vehicle_nsprefix_) else ''
            self.vehicle.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vehicle', pretty_print=pretty_print)
        if self.vessel is not None:
            namespaceprefix_ = self.vessel_nsprefix_ + ':' if (UseCapturedNS_ and self.vessel_nsprefix_) else ''
            self.vessel.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vessel', pretty_print=pretty_print)
        if self.aircraft is not None:
            namespaceprefix_ = self.aircraft_nsprefix_ + ':' if (UseCapturedNS_ and self.aircraft_nsprefix_) else ''
            self.aircraft.export(outfile, level, namespaceprefix_, namespacedef_='', name_='aircraft', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='NewTransportMeanType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.brand is not None:
            brand_ = self.brand
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}brand').text = self.gds_format_string(brand_)
        if self.serialNum is not None:
            serialNum_ = self.serialNum
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}serialNum').text = self.gds_format_string(serialNum_)
        if self.engineNum is not None:
            engineNum_ = self.engineNum
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}engineNum').text = self.gds_format_string(engineNum_)
        if self.firstEntryIntoService is not None:
            firstEntryIntoService_ = self.firstEntryIntoService
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}firstEntryIntoService').text = self.gds_format_date(firstEntryIntoService_)
        if self.vehicle is not None:
            vehicle_ = self.vehicle
            vehicle_.to_etree(element, name_='vehicle', mapping_=mapping_, nsmap_=nsmap_)
        if self.vessel is not None:
            vessel_ = self.vessel
            vessel_.to_etree(element, name_='vessel', mapping_=mapping_, nsmap_=nsmap_)
        if self.aircraft is not None:
            aircraft_ = self.aircraft
            aircraft_.to_etree(element, name_='aircraft', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='NewTransportMeanType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.brand is not None:
            showIndent(outfile, level)
            outfile.write('brand=%s,\n' % self.gds_encode(quote_python(self.brand)))
        if self.serialNum is not None:
            showIndent(outfile, level)
            outfile.write('serialNum=%s,\n' % self.gds_encode(quote_python(self.serialNum)))
        if self.engineNum is not None:
            showIndent(outfile, level)
            outfile.write('engineNum=%s,\n' % self.gds_encode(quote_python(self.engineNum)))
        if self.firstEntryIntoService is not None:
            showIndent(outfile, level)
            outfile.write('firstEntryIntoService=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.firstEntryIntoService, input_name='firstEntryIntoService'))
        if self.vehicle is not None:
            showIndent(outfile, level)
            outfile.write('vehicle=model_.VehicleType(\n')
            self.vehicle.exportLiteral(outfile, level, name_='vehicle')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vessel is not None:
            showIndent(outfile, level)
            outfile.write('vessel=model_.VesselType(\n')
            self.vessel.exportLiteral(outfile, level, name_='vessel')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.aircraft is not None:
            showIndent(outfile, level)
            outfile.write('aircraft=model_.AircraftType(\n')
            self.aircraft.exportLiteral(outfile, level, name_='aircraft')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'brand':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'brand')
            value_ = self.gds_validate_string(value_, node, 'brand')
            self.brand = value_
            self.brand_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.brand)
        elif nodeName_ == 'serialNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'serialNum')
            value_ = self.gds_validate_string(value_, node, 'serialNum')
            self.serialNum = value_
            self.serialNum_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.serialNum)
        elif nodeName_ == 'engineNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'engineNum')
            value_ = self.gds_validate_string(value_, node, 'engineNum')
            self.engineNum = value_
            self.engineNum_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.engineNum)
        elif nodeName_ == 'firstEntryIntoService':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.firstEntryIntoService = dval_
            self.firstEntryIntoService_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.firstEntryIntoService)
        elif nodeName_ == 'vehicle':
            obj_ = VehicleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vehicle = obj_
            obj_.original_tagname_ = 'vehicle'
        elif nodeName_ == 'vessel':
            obj_ = VesselType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vessel = obj_
            obj_.original_tagname_ = 'vessel'
        elif nodeName_ == 'aircraft':
            obj_ = AircraftType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.aircraft = obj_
            obj_.original_tagname_ = 'aircraft'
# end class NewTransportMeanType


class OrderNumbersType(GeneratedsSuper):
    """OrderNumbersType -- Megrendel
    é
    ssz
    á
    mok
    Order numbers
    orderNumber -- Megrendel
    é
    ssz
    á
    m
    Order number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, orderNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if orderNumber is None:
            self.orderNumber = []
        else:
            self.orderNumber = orderNumber
        self.orderNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OrderNumbersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OrderNumbersType.subclass:
            return OrderNumbersType.subclass(*args_, **kwargs_)
        else:
            return OrderNumbersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orderNumber(self):
        return self.orderNumber
    def set_orderNumber(self, orderNumber):
        self.orderNumber = orderNumber
    def add_orderNumber(self, value):
        self.orderNumber.append(value)
    def insert_orderNumber_at(self, index, value):
        self.orderNumber.insert(index, value)
    def replace_orderNumber_at(self, index, value):
        self.orderNumber[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.orderNumber
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='OrderNumbersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OrderNumbersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OrderNumbersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OrderNumbersType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OrderNumbersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OrderNumbersType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='OrderNumbersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for orderNumber_ in self.orderNumber:
            namespaceprefix_ = self.orderNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.orderNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sorderNumber>%s</%sorderNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(orderNumber_), input_name='orderNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='OrderNumbersType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for orderNumber_ in self.orderNumber:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}orderNumber').text = self.gds_format_string(orderNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='OrderNumbersType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('orderNumber=[\n')
        level += 1
        for orderNumber_ in self.orderNumber:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(orderNumber_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'orderNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'orderNumber')
            value_ = self.gds_validate_string(value_, node, 'orderNumber')
            self.orderNumber.append(value_)
            self.orderNumber_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.orderNumber[-1])
# end class OrderNumbersType


class PaymentEvidenceDocumentDataType(GeneratedsSuper):
    """PaymentEvidenceDocumentDataType -- A term
    é
    kd
    í
    j bevall
    á
    s
    á
    t igazol
    ó
    dokumentum adatai a 2011.
    é
    vi LXXXV. tv. 13.
    §
    (3) szerint
    é
    s a 25.
    §
    (3) szerint
    Data of the document verifying the declaration submitted on the product fee according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011
    evidenceDocumentNo -- Sz
    á
    mla sorsz
    á
    ma vagy egy
    é
    b okirat azonos
    í
    t
    ó
    sz
    á
    ma
    Sequential number of the invoice, or other document considered as such
    evidenceDocumentDate -- Sz
    á
    mla kelte
    Date of issue of the invoice
    obligatedName -- K
    ö
    telezett neve
    Name of obligator
    obligatedAddress -- K
    ö
    telezett c
    í
    me
    Address of obligator
    obligatedTaxNumber -- A k
    ö
    telezett ad
    ó
    sz
    á
    ma
    Tax number of obligated

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, evidenceDocumentNo=None, evidenceDocumentDate=None, obligatedName=None, obligatedAddress=None, obligatedTaxNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.evidenceDocumentNo = evidenceDocumentNo
        self.validate_SimpleText50NotBlankType(self.evidenceDocumentNo)
        self.evidenceDocumentNo_nsprefix_ = "common"
        if isinstance(evidenceDocumentDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(evidenceDocumentDate, '%Y-%m-%d').date()
        else:
            initvalue_ = evidenceDocumentDate
        self.evidenceDocumentDate = initvalue_
        self.evidenceDocumentDate_nsprefix_ = "base"
        self.obligatedName = obligatedName
        self.validate_SimpleText255NotBlankType(self.obligatedName)
        self.obligatedName_nsprefix_ = "common"
        self.obligatedAddress = obligatedAddress
        self.obligatedAddress_nsprefix_ = "base"
        self.obligatedTaxNumber = obligatedTaxNumber
        self.obligatedTaxNumber_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PaymentEvidenceDocumentDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PaymentEvidenceDocumentDataType.subclass:
            return PaymentEvidenceDocumentDataType.subclass(*args_, **kwargs_)
        else:
            return PaymentEvidenceDocumentDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_evidenceDocumentNo(self):
        return self.evidenceDocumentNo
    def set_evidenceDocumentNo(self, evidenceDocumentNo):
        self.evidenceDocumentNo = evidenceDocumentNo
    def get_evidenceDocumentDate(self):
        return self.evidenceDocumentDate
    def set_evidenceDocumentDate(self, evidenceDocumentDate):
        self.evidenceDocumentDate = evidenceDocumentDate
    def get_obligatedName(self):
        return self.obligatedName
    def set_obligatedName(self, obligatedName):
        self.obligatedName = obligatedName
    def get_obligatedAddress(self):
        return self.obligatedAddress
    def set_obligatedAddress(self, obligatedAddress):
        self.obligatedAddress = obligatedAddress
    def get_obligatedTaxNumber(self):
        return self.obligatedTaxNumber
    def set_obligatedTaxNumber(self, obligatedTaxNumber):
        self.obligatedTaxNumber = obligatedTaxNumber
    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_InvoiceDateType(self, value):
        result = True
        # Validate type InvoiceDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime.datetime.strptime('2010-01-01', '%Y-%m-%d').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceDateType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceDateType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceDateType_patterns_, ))
                result = False
        return result
    validate_InvoiceDateType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2})$']]
    def validate_SimpleText255NotBlankType(self, value):
        result = True
        # Validate type SimpleText255NotBlankType, a restriction on AtomicStringType255.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText255NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText255NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText255NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText255NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText255NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.evidenceDocumentNo is not None or
            self.evidenceDocumentDate is not None or
            self.obligatedName is not None or
            self.obligatedAddress is not None or
            self.obligatedTaxNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='PaymentEvidenceDocumentDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PaymentEvidenceDocumentDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PaymentEvidenceDocumentDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentEvidenceDocumentDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PaymentEvidenceDocumentDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PaymentEvidenceDocumentDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='PaymentEvidenceDocumentDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.evidenceDocumentNo is not None:
            namespaceprefix_ = self.evidenceDocumentNo_nsprefix_ + ':' if (UseCapturedNS_ and self.evidenceDocumentNo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevidenceDocumentNo>%s</%sevidenceDocumentNo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.evidenceDocumentNo), input_name='evidenceDocumentNo')), namespaceprefix_ , eol_))
        if self.evidenceDocumentDate is not None:
            namespaceprefix_ = self.evidenceDocumentDate_nsprefix_ + ':' if (UseCapturedNS_ and self.evidenceDocumentDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevidenceDocumentDate>%s</%sevidenceDocumentDate>%s' % (namespaceprefix_ , self.gds_format_date(self.evidenceDocumentDate, input_name='evidenceDocumentDate'), namespaceprefix_ , eol_))
        if self.obligatedName is not None:
            namespaceprefix_ = self.obligatedName_nsprefix_ + ':' if (UseCapturedNS_ and self.obligatedName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sobligatedName>%s</%sobligatedName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.obligatedName), input_name='obligatedName')), namespaceprefix_ , eol_))
        if self.obligatedAddress is not None:
            namespaceprefix_ = self.obligatedAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.obligatedAddress_nsprefix_) else ''
            self.obligatedAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='obligatedAddress', pretty_print=pretty_print)
        if self.obligatedTaxNumber is not None:
            namespaceprefix_ = self.obligatedTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.obligatedTaxNumber_nsprefix_) else ''
            self.obligatedTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='obligatedTaxNumber', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='PaymentEvidenceDocumentDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.evidenceDocumentNo is not None:
            evidenceDocumentNo_ = self.evidenceDocumentNo
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}evidenceDocumentNo').text = self.gds_format_string(evidenceDocumentNo_)
        if self.evidenceDocumentDate is not None:
            evidenceDocumentDate_ = self.evidenceDocumentDate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}evidenceDocumentDate').text = self.gds_format_date(evidenceDocumentDate_)
        if self.obligatedName is not None:
            obligatedName_ = self.obligatedName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}obligatedName').text = self.gds_format_string(obligatedName_)
        if self.obligatedAddress is not None:
            obligatedAddress_ = self.obligatedAddress
            obligatedAddress_.to_etree(element, name_='obligatedAddress', mapping_=mapping_, nsmap_=nsmap_)
        if self.obligatedTaxNumber is not None:
            obligatedTaxNumber_ = self.obligatedTaxNumber
            obligatedTaxNumber_.to_etree(element, name_='obligatedTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='PaymentEvidenceDocumentDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.evidenceDocumentNo is not None:
            showIndent(outfile, level)
            outfile.write('evidenceDocumentNo=%s,\n' % self.gds_encode(quote_python(self.evidenceDocumentNo)))
        if self.evidenceDocumentDate is not None:
            showIndent(outfile, level)
            outfile.write('evidenceDocumentDate=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.evidenceDocumentDate, input_name='evidenceDocumentDate'))
        if self.obligatedName is not None:
            showIndent(outfile, level)
            outfile.write('obligatedName=%s,\n' % self.gds_encode(quote_python(self.obligatedName)))
        if self.obligatedAddress is not None:
            showIndent(outfile, level)
            outfile.write('obligatedAddress=model_.AddressType(\n')
            self.obligatedAddress.exportLiteral(outfile, level, name_='obligatedAddress')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.obligatedTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('obligatedTaxNumber=model_.TaxNumberType(\n')
            self.obligatedTaxNumber.exportLiteral(outfile, level, name_='obligatedTaxNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'evidenceDocumentNo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'evidenceDocumentNo')
            value_ = self.gds_validate_string(value_, node, 'evidenceDocumentNo')
            self.evidenceDocumentNo = value_
            self.evidenceDocumentNo_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.evidenceDocumentNo)
        elif nodeName_ == 'evidenceDocumentDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.evidenceDocumentDate = dval_
            self.evidenceDocumentDate_nsprefix_ = child_.prefix
            # validate type InvoiceDateType
            self.validate_InvoiceDateType(self.evidenceDocumentDate)
        elif nodeName_ == 'obligatedName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'obligatedName')
            value_ = self.gds_validate_string(value_, node, 'obligatedName')
            self.obligatedName = value_
            self.obligatedName_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.obligatedName)
        elif nodeName_ == 'obligatedAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.obligatedAddress = obj_
            obj_.original_tagname_ = 'obligatedAddress'
        elif nodeName_ == 'obligatedTaxNumber':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.obligatedTaxNumber = obj_
            obj_.original_tagname_ = 'obligatedTaxNumber'
# end class PaymentEvidenceDocumentDataType


class ProductCodesType(GeneratedsSuper):
    """ProductCodesType -- Term
    é
    kk
    ó
    dok
    Product codes
    productCode -- Term
    é
    kk
    ó
    d
    Product code

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if productCode is None:
            self.productCode = []
        else:
            self.productCode = productCode
        self.productCode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductCodesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductCodesType.subclass:
            return ProductCodesType.subclass(*args_, **kwargs_)
        else:
            return ProductCodesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productCode(self):
        return self.productCode
    def set_productCode(self, productCode):
        self.productCode = productCode
    def add_productCode(self, value):
        self.productCode.append(value)
    def insert_productCode_at(self, index, value):
        self.productCode.insert(index, value)
    def replace_productCode_at(self, index, value):
        self.productCode[index] = value
    def _hasContent(self):
        if (
            self.productCode
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ProductCodesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductCodesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductCodesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductCodesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductCodesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductCodesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ProductCodesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for productCode_ in self.productCode:
            namespaceprefix_ = self.productCode_nsprefix_ + ':' if (UseCapturedNS_ and self.productCode_nsprefix_) else ''
            productCode_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productCode', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ProductCodesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for productCode_ in self.productCode:
            productCode_.to_etree(element, name_='productCode', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductCodesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('productCode=[\n')
        level += 1
        for productCode_ in self.productCode:
            showIndent(outfile, level)
            outfile.write('model_.ProductCodeType(\n')
            productCode_.exportLiteral(outfile, level, name_='ProductCodeType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'productCode':
            obj_ = ProductCodeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productCode.append(obj_)
            obj_.original_tagname_ = 'productCode'
# end class ProductCodesType


class ProductCodeType(GeneratedsSuper):
    """ProductCodeType -- K
    ü
    l
    ö
    nb
    ö
    z
    ő
    term
    é
    k- vagy szolg
    á
    ltat
    á
    sk
    ó
    dokat tartalmaz
    ó
    t
    í
    pus
    Field type including the different product and service codes
    productCodeCategory -- A term
    é
    kk
    ó
    d fajt
    á
    j
    á
    nak (pl. VTSZ, CsK, stb.) jel
    ö
    l
    é
    se
    The kind of product code (f. ex. VTSZ, CsK, etc.)
    productCodeValue -- A term
    é
    kk
    ó
    d
    é
    rt
    é
    ke nem saj
    á
    t term
    é
    kk
    ó
    d eset
    é
    n
    The value of (not own) product code
    productCodeOwnValue -- Saj
    á
    t term
    é
    kk
    ó
    d
    é
    rt
    é
    ke
    Own product code value

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productCodeCategory=None, productCodeValue=None, productCodeOwnValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.productCodeCategory = productCodeCategory
        self.validate_ProductCodeCategoryType(self.productCodeCategory)
        self.productCodeCategory_nsprefix_ = None
        self.productCodeValue = productCodeValue
        self.validate_ProductCodeValueType(self.productCodeValue)
        self.productCodeValue_nsprefix_ = None
        self.productCodeOwnValue = productCodeOwnValue
        self.validate_SimpleText255NotBlankType(self.productCodeOwnValue)
        self.productCodeOwnValue_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductCodeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductCodeType.subclass:
            return ProductCodeType.subclass(*args_, **kwargs_)
        else:
            return ProductCodeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productCodeCategory(self):
        return self.productCodeCategory
    def set_productCodeCategory(self, productCodeCategory):
        self.productCodeCategory = productCodeCategory
    def get_productCodeValue(self):
        return self.productCodeValue
    def set_productCodeValue(self, productCodeValue):
        self.productCodeValue = productCodeValue
    def get_productCodeOwnValue(self):
        return self.productCodeOwnValue
    def set_productCodeOwnValue(self, productCodeOwnValue):
        self.productCodeOwnValue = productCodeOwnValue
    def validate_ProductCodeCategoryType(self, value):
        result = True
        # Validate type ProductCodeCategoryType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['VTSZ', 'SZJ', 'KN', 'AHK', 'CSK', 'KT', 'EJ', 'TESZOR', 'OWN', 'OTHER']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductCodeCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductCodeCategoryType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductCodeCategoryType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductCodeCategoryType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductCodeCategoryType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_ProductCodeValueType(self, value):
        result = True
        # Validate type ProductCodeValueType, a restriction on common:AtomicStringType32.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductCodeValueType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductCodeValueType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductCodeValueType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductCodeValueType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ProductCodeValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ProductCodeValueType_patterns_, ))
                result = False
        return result
    validate_ProductCodeValueType_patterns_ = [['^([A-Z0-9]{2,30})$']]
    def validate_SimpleText255NotBlankType(self, value):
        result = True
        # Validate type SimpleText255NotBlankType, a restriction on AtomicStringType255.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText255NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText255NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText255NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText255NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText255NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.productCodeCategory is not None or
            self.productCodeValue is not None or
            self.productCodeOwnValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ProductCodeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductCodeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductCodeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductCodeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductCodeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductCodeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ProductCodeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.productCodeCategory is not None:
            namespaceprefix_ = self.productCodeCategory_nsprefix_ + ':' if (UseCapturedNS_ and self.productCodeCategory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductCodeCategory>%s</%sproductCodeCategory>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productCodeCategory), input_name='productCodeCategory')), namespaceprefix_ , eol_))
        if self.productCodeValue is not None:
            namespaceprefix_ = self.productCodeValue_nsprefix_ + ':' if (UseCapturedNS_ and self.productCodeValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductCodeValue>%s</%sproductCodeValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productCodeValue), input_name='productCodeValue')), namespaceprefix_ , eol_))
        if self.productCodeOwnValue is not None:
            namespaceprefix_ = self.productCodeOwnValue_nsprefix_ + ':' if (UseCapturedNS_ and self.productCodeOwnValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductCodeOwnValue>%s</%sproductCodeOwnValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productCodeOwnValue), input_name='productCodeOwnValue')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ProductCodeType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.productCodeCategory is not None:
            productCodeCategory_ = self.productCodeCategory
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productCodeCategory').text = self.gds_format_string(productCodeCategory_)
        if self.productCodeValue is not None:
            productCodeValue_ = self.productCodeValue
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productCodeValue').text = self.gds_format_string(productCodeValue_)
        if self.productCodeOwnValue is not None:
            productCodeOwnValue_ = self.productCodeOwnValue
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productCodeOwnValue').text = self.gds_format_string(productCodeOwnValue_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductCodeType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.productCodeCategory is not None:
            showIndent(outfile, level)
            outfile.write('productCodeCategory=%s,\n' % self.gds_encode(quote_python(self.productCodeCategory)))
        if self.productCodeValue is not None:
            showIndent(outfile, level)
            outfile.write('productCodeValue=%s,\n' % self.gds_encode(quote_python(self.productCodeValue)))
        if self.productCodeOwnValue is not None:
            showIndent(outfile, level)
            outfile.write('productCodeOwnValue=%s,\n' % self.gds_encode(quote_python(self.productCodeOwnValue)))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'productCodeCategory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productCodeCategory')
            value_ = self.gds_validate_string(value_, node, 'productCodeCategory')
            self.productCodeCategory = value_
            self.productCodeCategory_nsprefix_ = child_.prefix
            # validate type ProductCodeCategoryType
            self.validate_ProductCodeCategoryType(self.productCodeCategory)
        elif nodeName_ == 'productCodeValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productCodeValue')
            value_ = self.gds_validate_string(value_, node, 'productCodeValue')
            self.productCodeValue = value_
            self.productCodeValue_nsprefix_ = child_.prefix
            # validate type ProductCodeValueType
            self.validate_ProductCodeValueType(self.productCodeValue)
        elif nodeName_ == 'productCodeOwnValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productCodeOwnValue')
            value_ = self.gds_validate_string(value_, node, 'productCodeOwnValue')
            self.productCodeOwnValue = value_
            self.productCodeOwnValue_nsprefix_ = child_.prefix
            # validate type SimpleText255NotBlankType
            self.validate_SimpleText255NotBlankType(self.productCodeOwnValue)
# end class ProductCodeType


class ProductFeeClauseType(GeneratedsSuper):
    """ProductFeeClauseType -- A k
    ö
    rnyezetv
    é
    delmi term
    é
    kd
    í
    jr
    ó
    l sz
    ó
    l
    ó
    2011.
    é
    vi LXXXV. tv. szerinti, t
    é
    telre vonatkoz
    ó
    z
    á
    rad
    é
    kok
    Clauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)
    productFeeTakeoverData -- A k
    ö
    rnyezetv
    é
    delmi term
    é
    kd
    í
    j k
    ö
    telezetts
    é
    g
    á
    tv
    á
    llal
    á
    s
    á
    val kapcsolatos adatok
    Data in connection with takeover of environmental protection product fee
    customerDeclaration -- Ha az elad
    ó
    a vev
    ő
    nyilatkozata alapj
    á
    n mentes
    ü
    l a term
    é
    kd
    í
    j megfizet
    é
    se al
    ó
    l, akkor az
    é
    rintett term
    é
    k
    á
    ram
    Should the supplier, based on statement given by the purchaser, be exempted from paying product fee, then the product stream affected

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productFeeTakeoverData=None, customerDeclaration=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.productFeeTakeoverData = productFeeTakeoverData
        self.productFeeTakeoverData_nsprefix_ = None
        self.customerDeclaration = customerDeclaration
        self.customerDeclaration_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductFeeClauseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductFeeClauseType.subclass:
            return ProductFeeClauseType.subclass(*args_, **kwargs_)
        else:
            return ProductFeeClauseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productFeeTakeoverData(self):
        return self.productFeeTakeoverData
    def set_productFeeTakeoverData(self, productFeeTakeoverData):
        self.productFeeTakeoverData = productFeeTakeoverData
    def get_customerDeclaration(self):
        return self.customerDeclaration
    def set_customerDeclaration(self, customerDeclaration):
        self.customerDeclaration = customerDeclaration
    def _hasContent(self):
        if (
            self.productFeeTakeoverData is not None or
            self.customerDeclaration is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ProductFeeClauseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductFeeClauseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductFeeClauseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductFeeClauseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductFeeClauseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductFeeClauseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='ProductFeeClauseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.productFeeTakeoverData is not None:
            namespaceprefix_ = self.productFeeTakeoverData_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeTakeoverData_nsprefix_) else ''
            self.productFeeTakeoverData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productFeeTakeoverData', pretty_print=pretty_print)
        if self.customerDeclaration is not None:
            namespaceprefix_ = self.customerDeclaration_nsprefix_ + ':' if (UseCapturedNS_ and self.customerDeclaration_nsprefix_) else ''
            self.customerDeclaration.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customerDeclaration', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ProductFeeClauseType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.productFeeTakeoverData is not None:
            productFeeTakeoverData_ = self.productFeeTakeoverData
            productFeeTakeoverData_.to_etree(element, name_='productFeeTakeoverData', mapping_=mapping_, nsmap_=nsmap_)
        if self.customerDeclaration is not None:
            customerDeclaration_ = self.customerDeclaration
            customerDeclaration_.to_etree(element, name_='customerDeclaration', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductFeeClauseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.productFeeTakeoverData is not None:
            showIndent(outfile, level)
            outfile.write('productFeeTakeoverData=model_.ProductFeeTakeoverDataType(\n')
            self.productFeeTakeoverData.exportLiteral(outfile, level, name_='productFeeTakeoverData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.customerDeclaration is not None:
            showIndent(outfile, level)
            outfile.write('customerDeclaration=model_.CustomerDeclarationType(\n')
            self.customerDeclaration.exportLiteral(outfile, level, name_='customerDeclaration')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'productFeeTakeoverData':
            obj_ = ProductFeeTakeoverDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productFeeTakeoverData = obj_
            obj_.original_tagname_ = 'productFeeTakeoverData'
        elif nodeName_ == 'customerDeclaration':
            obj_ = CustomerDeclarationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerDeclaration = obj_
            obj_.original_tagname_ = 'customerDeclaration'
# end class ProductFeeClauseType


class ProductFeeDataType(GeneratedsSuper):
    """ProductFeeDataType -- Term
    é
    kd
    í
    j adatok
    Product charges data
    productFeeCode -- Term
    é
    kd
    í
    j k
    ó
    d (Kt vagy Csk)
    Product charges code (Kt or Csk code)
    productFeeQuantity -- A term
    é
    kd
    í
    jjal
    é
    rintett term
    é
    k mennyis
    é
    ge
    Quantity of product, according to product charge
    productFeeMeasuringUnit -- A d
    í
    jt
    é
    tel egys
    é
    ge (kg vagy darab)
    Unit of the rate (kg or piece)
    productFeeRate -- A term
    é
    kd
    í
    j d
    í
    jt
    é
    tele (HUF/egys
    é
    g)
    Product fee rate (HUF/unit)
    productFeeAmount -- Term
    é
    kd
    í
    j
    ö
    sszege forintban
    Amount in Hungarian forints of the product fee

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productFeeCode=None, productFeeQuantity=None, productFeeMeasuringUnit=None, productFeeRate=None, productFeeAmount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.productFeeCode = productFeeCode
        self.productFeeCode_nsprefix_ = None
        self.productFeeQuantity = productFeeQuantity
        self.validate_QuantityType(self.productFeeQuantity)
        self.productFeeQuantity_nsprefix_ = None
        self.productFeeMeasuringUnit = productFeeMeasuringUnit
        self.validate_ProductFeeMeasuringUnitType(self.productFeeMeasuringUnit)
        self.productFeeMeasuringUnit_nsprefix_ = None
        self.productFeeRate = productFeeRate
        self.validate_MonetaryType(self.productFeeRate)
        self.productFeeRate_nsprefix_ = "base"
        self.productFeeAmount = productFeeAmount
        self.validate_MonetaryType(self.productFeeAmount)
        self.productFeeAmount_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductFeeDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductFeeDataType.subclass:
            return ProductFeeDataType.subclass(*args_, **kwargs_)
        else:
            return ProductFeeDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productFeeCode(self):
        return self.productFeeCode
    def set_productFeeCode(self, productFeeCode):
        self.productFeeCode = productFeeCode
    def get_productFeeQuantity(self):
        return self.productFeeQuantity
    def set_productFeeQuantity(self, productFeeQuantity):
        self.productFeeQuantity = productFeeQuantity
    def get_productFeeMeasuringUnit(self):
        return self.productFeeMeasuringUnit
    def set_productFeeMeasuringUnit(self, productFeeMeasuringUnit):
        self.productFeeMeasuringUnit = productFeeMeasuringUnit
    def get_productFeeRate(self):
        return self.productFeeRate
    def set_productFeeRate(self, productFeeRate):
        self.productFeeRate = productFeeRate
    def get_productFeeAmount(self):
        return self.productFeeAmount
    def set_productFeeAmount(self, productFeeAmount):
        self.productFeeAmount = productFeeAmount
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_ProductFeeMeasuringUnitType(self, value):
        result = True
        # Validate type ProductFeeMeasuringUnitType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['DARAB', 'KG']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductFeeMeasuringUnitType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductFeeMeasuringUnitType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductFeeMeasuringUnitType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.productFeeCode is not None or
            self.productFeeQuantity is not None or
            self.productFeeMeasuringUnit is not None or
            self.productFeeRate is not None or
            self.productFeeAmount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductFeeDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductFeeDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductFeeDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductFeeDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductFeeDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.productFeeCode is not None:
            namespaceprefix_ = self.productFeeCode_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeCode_nsprefix_) else ''
            self.productFeeCode.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productFeeCode', pretty_print=pretty_print)
        if self.productFeeQuantity is not None:
            namespaceprefix_ = self.productFeeQuantity_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeQuantity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeQuantity>%s</%sproductFeeQuantity>%s' % (namespaceprefix_ , self.gds_format_decimal(self.productFeeQuantity, input_name='productFeeQuantity'), namespaceprefix_ , eol_))
        if self.productFeeMeasuringUnit is not None:
            namespaceprefix_ = self.productFeeMeasuringUnit_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeMeasuringUnit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeMeasuringUnit>%s</%sproductFeeMeasuringUnit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productFeeMeasuringUnit), input_name='productFeeMeasuringUnit')), namespaceprefix_ , eol_))
        if self.productFeeRate is not None:
            namespaceprefix_ = self.productFeeRate_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeRate>%s</%sproductFeeRate>%s' % (namespaceprefix_ , self.gds_format_decimal(self.productFeeRate, input_name='productFeeRate'), namespaceprefix_ , eol_))
        if self.productFeeAmount is not None:
            namespaceprefix_ = self.productFeeAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeAmount>%s</%sproductFeeAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.productFeeAmount, input_name='productFeeAmount'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ProductFeeDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.productFeeCode is not None:
            productFeeCode_ = self.productFeeCode
            productFeeCode_.to_etree(element, name_='productFeeCode', mapping_=mapping_, nsmap_=nsmap_)
        if self.productFeeQuantity is not None:
            productFeeQuantity_ = self.productFeeQuantity
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeQuantity').text = self.gds_format_decimal(productFeeQuantity_)
        if self.productFeeMeasuringUnit is not None:
            productFeeMeasuringUnit_ = self.productFeeMeasuringUnit
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeMeasuringUnit').text = self.gds_format_string(productFeeMeasuringUnit_)
        if self.productFeeRate is not None:
            productFeeRate_ = self.productFeeRate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeRate').text = self.gds_format_decimal(productFeeRate_)
        if self.productFeeAmount is not None:
            productFeeAmount_ = self.productFeeAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeAmount').text = self.gds_format_decimal(productFeeAmount_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductFeeDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.productFeeCode is not None:
            showIndent(outfile, level)
            outfile.write('productFeeCode=model_.ProductCodeType(\n')
            self.productFeeCode.exportLiteral(outfile, level, name_='productFeeCode')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.productFeeQuantity is not None:
            showIndent(outfile, level)
            outfile.write('productFeeQuantity=%f,\n' % self.productFeeQuantity)
        if self.productFeeMeasuringUnit is not None:
            showIndent(outfile, level)
            outfile.write('productFeeMeasuringUnit=%s,\n' % self.gds_encode(quote_python(self.productFeeMeasuringUnit)))
        if self.productFeeRate is not None:
            showIndent(outfile, level)
            outfile.write('productFeeRate=%f,\n' % self.productFeeRate)
        if self.productFeeAmount is not None:
            showIndent(outfile, level)
            outfile.write('productFeeAmount=%f,\n' % self.productFeeAmount)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'productFeeCode':
            obj_ = ProductCodeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productFeeCode = obj_
            obj_.original_tagname_ = 'productFeeCode'
        elif nodeName_ == 'productFeeQuantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'productFeeQuantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'productFeeQuantity')
            self.productFeeQuantity = fval_
            self.productFeeQuantity_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.productFeeQuantity)
        elif nodeName_ == 'productFeeMeasuringUnit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productFeeMeasuringUnit')
            value_ = self.gds_validate_string(value_, node, 'productFeeMeasuringUnit')
            self.productFeeMeasuringUnit = value_
            self.productFeeMeasuringUnit_nsprefix_ = child_.prefix
            # validate type ProductFeeMeasuringUnitType
            self.validate_ProductFeeMeasuringUnitType(self.productFeeMeasuringUnit)
        elif nodeName_ == 'productFeeRate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'productFeeRate')
            fval_ = self.gds_validate_decimal(fval_, node, 'productFeeRate')
            self.productFeeRate = fval_
            self.productFeeRate_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.productFeeRate)
        elif nodeName_ == 'productFeeAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'productFeeAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'productFeeAmount')
            self.productFeeAmount = fval_
            self.productFeeAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.productFeeAmount)
# end class ProductFeeDataType


class ProductFeeSummaryType(GeneratedsSuper):
    """ProductFeeSummaryType -- Term
    é
    kd
    í
    j
    ö
    sszegz
    é
    s adatok
    Summary of product charges
    productFeeOperation -- Annak jelz
    é
    se, hogy a term
    é
    kd
    í
    j
    ö
    sszes
    í
    t
    é
    s visszaig
    é
    nyl
    é
    sre (REFUND) vagy rakt
    á
    rba t
    ö
    rt
    é
    n
    ő
    besz
    á
    ll
    í
    t
    á
    sra (DEPOSIT) vonatkozik
    Indicating whether the the product fee summary concerns refund or deposit
    productFeeData -- Term
    é
    kd
    í
    j adatok
    Product charges data
    productChargeSum -- Term
    é
    kd
    í
    j
    ö
    sszesen
    Aggregate product charges
    paymentEvidenceDocumentData -- A term
    é
    kd
    í
    j bevall
    á
    s
    á
    t igazol
    ó
    dokumentum adatai a 2011.
    é
    vi LXXXV. tv. 13.
    §
    (3) szerint
    é
    s a 25.
    §
    (3) szerint
    Data of the document verifying the declaration submitted on the product fee according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, productFeeOperation=None, productFeeData=None, productChargeSum=None, paymentEvidenceDocumentData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.productFeeOperation = productFeeOperation
        self.validate_ProductFeeOperationType(self.productFeeOperation)
        self.productFeeOperation_nsprefix_ = None
        if productFeeData is None:
            self.productFeeData = []
        else:
            self.productFeeData = productFeeData
        self.productFeeData_nsprefix_ = None
        self.productChargeSum = productChargeSum
        self.validate_MonetaryType(self.productChargeSum)
        self.productChargeSum_nsprefix_ = "base"
        self.paymentEvidenceDocumentData = paymentEvidenceDocumentData
        self.paymentEvidenceDocumentData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductFeeSummaryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductFeeSummaryType.subclass:
            return ProductFeeSummaryType.subclass(*args_, **kwargs_)
        else:
            return ProductFeeSummaryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_productFeeOperation(self):
        return self.productFeeOperation
    def set_productFeeOperation(self, productFeeOperation):
        self.productFeeOperation = productFeeOperation
    def get_productFeeData(self):
        return self.productFeeData
    def set_productFeeData(self, productFeeData):
        self.productFeeData = productFeeData
    def add_productFeeData(self, value):
        self.productFeeData.append(value)
    def insert_productFeeData_at(self, index, value):
        self.productFeeData.insert(index, value)
    def replace_productFeeData_at(self, index, value):
        self.productFeeData[index] = value
    def get_productChargeSum(self):
        return self.productChargeSum
    def set_productChargeSum(self, productChargeSum):
        self.productChargeSum = productChargeSum
    def get_paymentEvidenceDocumentData(self):
        return self.paymentEvidenceDocumentData
    def set_paymentEvidenceDocumentData(self, paymentEvidenceDocumentData):
        self.paymentEvidenceDocumentData = paymentEvidenceDocumentData
    def validate_ProductFeeOperationType(self, value):
        result = True
        # Validate type ProductFeeOperationType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['REFUND', 'DEPOSIT']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductFeeOperationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProductFeeOperationType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProductFeeOperationType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.productFeeOperation is not None or
            self.productFeeData or
            self.productChargeSum is not None or
            self.paymentEvidenceDocumentData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeSummaryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductFeeSummaryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductFeeSummaryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductFeeSummaryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductFeeSummaryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductFeeSummaryType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeSummaryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.productFeeOperation is not None:
            namespaceprefix_ = self.productFeeOperation_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeOperation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductFeeOperation>%s</%sproductFeeOperation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.productFeeOperation), input_name='productFeeOperation')), namespaceprefix_ , eol_))
        for productFeeData_ in self.productFeeData:
            namespaceprefix_ = self.productFeeData_nsprefix_ + ':' if (UseCapturedNS_ and self.productFeeData_nsprefix_) else ''
            productFeeData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='productFeeData', pretty_print=pretty_print)
        if self.productChargeSum is not None:
            namespaceprefix_ = self.productChargeSum_nsprefix_ + ':' if (UseCapturedNS_ and self.productChargeSum_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproductChargeSum>%s</%sproductChargeSum>%s' % (namespaceprefix_ , self.gds_format_decimal(self.productChargeSum, input_name='productChargeSum'), namespaceprefix_ , eol_))
        if self.paymentEvidenceDocumentData is not None:
            namespaceprefix_ = self.paymentEvidenceDocumentData_nsprefix_ + ':' if (UseCapturedNS_ and self.paymentEvidenceDocumentData_nsprefix_) else ''
            self.paymentEvidenceDocumentData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='paymentEvidenceDocumentData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ProductFeeSummaryType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.productFeeOperation is not None:
            productFeeOperation_ = self.productFeeOperation
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productFeeOperation').text = self.gds_format_string(productFeeOperation_)
        for productFeeData_ in self.productFeeData:
            productFeeData_.to_etree(element, name_='productFeeData', mapping_=mapping_, nsmap_=nsmap_)
        if self.productChargeSum is not None:
            productChargeSum_ = self.productChargeSum
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}productChargeSum').text = self.gds_format_decimal(productChargeSum_)
        if self.paymentEvidenceDocumentData is not None:
            paymentEvidenceDocumentData_ = self.paymentEvidenceDocumentData
            paymentEvidenceDocumentData_.to_etree(element, name_='paymentEvidenceDocumentData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductFeeSummaryType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.productFeeOperation is not None:
            showIndent(outfile, level)
            outfile.write('productFeeOperation=%s,\n' % self.gds_encode(quote_python(self.productFeeOperation)))
        showIndent(outfile, level)
        outfile.write('productFeeData=[\n')
        level += 1
        for productFeeData_ in self.productFeeData:
            showIndent(outfile, level)
            outfile.write('model_.ProductFeeDataType(\n')
            productFeeData_.exportLiteral(outfile, level, name_='ProductFeeDataType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.productChargeSum is not None:
            showIndent(outfile, level)
            outfile.write('productChargeSum=%f,\n' % self.productChargeSum)
        if self.paymentEvidenceDocumentData is not None:
            showIndent(outfile, level)
            outfile.write('paymentEvidenceDocumentData=model_.PaymentEvidenceDocumentDataType(\n')
            self.paymentEvidenceDocumentData.exportLiteral(outfile, level, name_='paymentEvidenceDocumentData')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'productFeeOperation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'productFeeOperation')
            value_ = self.gds_validate_string(value_, node, 'productFeeOperation')
            self.productFeeOperation = value_
            self.productFeeOperation_nsprefix_ = child_.prefix
            # validate type ProductFeeOperationType
            self.validate_ProductFeeOperationType(self.productFeeOperation)
        elif nodeName_ == 'productFeeData':
            obj_ = ProductFeeDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.productFeeData.append(obj_)
            obj_.original_tagname_ = 'productFeeData'
        elif nodeName_ == 'productChargeSum' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'productChargeSum')
            fval_ = self.gds_validate_decimal(fval_, node, 'productChargeSum')
            self.productChargeSum = fval_
            self.productChargeSum_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.productChargeSum)
        elif nodeName_ == 'paymentEvidenceDocumentData':
            obj_ = PaymentEvidenceDocumentDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.paymentEvidenceDocumentData = obj_
            obj_.original_tagname_ = 'paymentEvidenceDocumentData'
# end class ProductFeeSummaryType


class ProductFeeTakeoverDataType(GeneratedsSuper):
    """ProductFeeTakeoverDataType -- A k
    ö
    rnyezetv
    é
    delmi term
    é
    kd
    í
    j k
    ö
    telezetts
    é
    g
    á
    tv
    á
    llal
    á
    s
    á
    val kapcsolatos adatok
    Data in connection with takeover of environmental protection product fee
    takeoverReason -- Az
    á
    tv
    á
    llal
    á
    s ir
    á
    nya
    é
    s jogszab
    á
    lyi alapja
    Direction and legal base of takeover
    takeoverAmount -- Az
    á
    tv
    á
    llalt term
    é
    kd
    í
    j
    ö
    sszege forintban, ha a vev
    ő
    v
    á
    llalja
    á
    t az elad
    ó
    term
    é
    kd
    í
    j-k
    ö
    telezetts
    é
    g
    é
    t
    Amount in Hungarian forints of the product fee taken over if the purchaser takes over the supplier
    ’
    s product fee liability

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, takeoverReason=None, takeoverAmount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.takeoverReason = takeoverReason
        self.validate_TakeoverType(self.takeoverReason)
        self.takeoverReason_nsprefix_ = None
        self.takeoverAmount = takeoverAmount
        self.validate_MonetaryType(self.takeoverAmount)
        self.takeoverAmount_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProductFeeTakeoverDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProductFeeTakeoverDataType.subclass:
            return ProductFeeTakeoverDataType.subclass(*args_, **kwargs_)
        else:
            return ProductFeeTakeoverDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_takeoverReason(self):
        return self.takeoverReason
    def set_takeoverReason(self, takeoverReason):
        self.takeoverReason = takeoverReason
    def get_takeoverAmount(self):
        return self.takeoverAmount
    def set_takeoverAmount(self, takeoverAmount):
        self.takeoverAmount = takeoverAmount
    def validate_TakeoverType(self, value):
        result = True
        # Validate type TakeoverType, a restriction on common:AtomicStringType8.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['01', '02_aa', '02_ab', '02_b', '02_c', '02_d', '02_ea', '02_eb', '02_fa', '02_fb', '02_ga', '02_gb']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TakeoverType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TakeoverType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TakeoverType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.takeoverReason is not None or
            self.takeoverAmount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeTakeoverDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProductFeeTakeoverDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProductFeeTakeoverDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProductFeeTakeoverDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProductFeeTakeoverDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProductFeeTakeoverDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ProductFeeTakeoverDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.takeoverReason is not None:
            namespaceprefix_ = self.takeoverReason_nsprefix_ + ':' if (UseCapturedNS_ and self.takeoverReason_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stakeoverReason>%s</%stakeoverReason>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.takeoverReason), input_name='takeoverReason')), namespaceprefix_ , eol_))
        if self.takeoverAmount is not None:
            namespaceprefix_ = self.takeoverAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.takeoverAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stakeoverAmount>%s</%stakeoverAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.takeoverAmount, input_name='takeoverAmount'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ProductFeeTakeoverDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.takeoverReason is not None:
            takeoverReason_ = self.takeoverReason
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}takeoverReason').text = self.gds_format_string(takeoverReason_)
        if self.takeoverAmount is not None:
            takeoverAmount_ = self.takeoverAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}takeoverAmount').text = self.gds_format_decimal(takeoverAmount_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProductFeeTakeoverDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.takeoverReason is not None:
            showIndent(outfile, level)
            outfile.write('takeoverReason=%s,\n' % self.gds_encode(quote_python(self.takeoverReason)))
        if self.takeoverAmount is not None:
            showIndent(outfile, level)
            outfile.write('takeoverAmount=%f,\n' % self.takeoverAmount)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'takeoverReason':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'takeoverReason')
            value_ = self.gds_validate_string(value_, node, 'takeoverReason')
            self.takeoverReason = value_
            self.takeoverReason_nsprefix_ = child_.prefix
            # validate type TakeoverType
            self.validate_TakeoverType(self.takeoverReason)
        elif nodeName_ == 'takeoverAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'takeoverAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'takeoverAmount')
            self.takeoverAmount = fval_
            self.takeoverAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.takeoverAmount)
# end class ProductFeeTakeoverDataType


class ProjectNumbersType(GeneratedsSuper):
    """ProjectNumbersType -- Projektsz
    á
    mok
    Project numbers
    projectNumber -- Projektsz
    á
    m
    Project number

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, projectNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if projectNumber is None:
            self.projectNumber = []
        else:
            self.projectNumber = projectNumber
        self.projectNumber_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProjectNumbersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProjectNumbersType.subclass:
            return ProjectNumbersType.subclass(*args_, **kwargs_)
        else:
            return ProjectNumbersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_projectNumber(self):
        return self.projectNumber
    def set_projectNumber(self, projectNumber):
        self.projectNumber = projectNumber
    def add_projectNumber(self, value):
        self.projectNumber.append(value)
    def insert_projectNumber_at(self, index, value):
        self.projectNumber.insert(index, value)
    def replace_projectNumber_at(self, index, value):
        self.projectNumber[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.projectNumber
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ProjectNumbersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProjectNumbersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProjectNumbersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProjectNumbersType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProjectNumbersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProjectNumbersType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ProjectNumbersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for projectNumber_ in self.projectNumber:
            namespaceprefix_ = self.projectNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.projectNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprojectNumber>%s</%sprojectNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(projectNumber_), input_name='projectNumber')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ProjectNumbersType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for projectNumber_ in self.projectNumber:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}projectNumber').text = self.gds_format_string(projectNumber_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ProjectNumbersType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('projectNumber=[\n')
        level += 1
        for projectNumber_ in self.projectNumber:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(projectNumber_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'projectNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'projectNumber')
            value_ = self.gds_validate_string(value_, node, 'projectNumber')
            self.projectNumber.append(value_)
            self.projectNumber_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.projectNumber[-1])
# end class ProjectNumbersType


class ReferencesToOtherLinesType(GeneratedsSuper):
    """ReferencesToOtherLinesType -- Hivatkoz
    á
    sok kapcsol
    ó
    d
    ó
    t
    é
    telekre, ha ez az
    Á
    FA t
    ö
    rv
    é
    ny alapj
    á
    n sz
    ü
    ks
    é
    ges
    References to connected items if it is necessary according to VAT law
    referenceToOtherLine -- Hivatkoz
    á
    sok kapcsol
    ó
    d
    ó
    t
    é
    telekre, ha ez az
    Á
    FA t
    ö
    rv
    é
    ny alapj
    á
    n sz
    ü
    ks
    é
    ges
    References to connected items if it is necessary according to VAT law

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, referenceToOtherLine=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if referenceToOtherLine is None:
            self.referenceToOtherLine = []
        else:
            self.referenceToOtherLine = referenceToOtherLine
        self.referenceToOtherLine_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReferencesToOtherLinesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReferencesToOtherLinesType.subclass:
            return ReferencesToOtherLinesType.subclass(*args_, **kwargs_)
        else:
            return ReferencesToOtherLinesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_referenceToOtherLine(self):
        return self.referenceToOtherLine
    def set_referenceToOtherLine(self, referenceToOtherLine):
        self.referenceToOtherLine = referenceToOtherLine
    def add_referenceToOtherLine(self, value):
        self.referenceToOtherLine.append(value)
    def insert_referenceToOtherLine_at(self, index, value):
        self.referenceToOtherLine.insert(index, value)
    def replace_referenceToOtherLine_at(self, index, value):
        self.referenceToOtherLine[index] = value
    def validate_LineNumberType(self, value):
        result = True
        # Validate type LineNumberType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on LineNumberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.referenceToOtherLine
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ReferencesToOtherLinesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReferencesToOtherLinesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReferencesToOtherLinesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferencesToOtherLinesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferencesToOtherLinesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ReferencesToOtherLinesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='ReferencesToOtherLinesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for referenceToOtherLine_ in self.referenceToOtherLine:
            namespaceprefix_ = self.referenceToOtherLine_nsprefix_ + ':' if (UseCapturedNS_ and self.referenceToOtherLine_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreferenceToOtherLine>%s</%sreferenceToOtherLine>%s' % (namespaceprefix_ , self.gds_format_integer(referenceToOtherLine_, input_name='referenceToOtherLine'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ReferencesToOtherLinesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for referenceToOtherLine_ in self.referenceToOtherLine:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}referenceToOtherLine').text = self.gds_format_integer(referenceToOtherLine_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ReferencesToOtherLinesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('referenceToOtherLine=[\n')
        level += 1
        for referenceToOtherLine_ in self.referenceToOtherLine:
            showIndent(outfile, level)
            outfile.write('%d,\n' % referenceToOtherLine_)
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'referenceToOtherLine' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'referenceToOtherLine')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'referenceToOtherLine')
            self.referenceToOtherLine.append(ival_)
            self.referenceToOtherLine_nsprefix_ = child_.prefix
            # validate type LineNumberType
            self.validate_LineNumberType(self.referenceToOtherLine[-1])
# end class ReferencesToOtherLinesType


class ShippingDatesType(GeneratedsSuper):
    """ShippingDatesType -- Sz
    á
    ll
    í
    t
    á
    si d
    á
    tumok
    Shipping dates
    shippingDate -- Sz
    á
    ll
    í
    t
    á
    si d
    á
    tum
    Shipping date

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, shippingDate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if shippingDate is None:
            self.shippingDate = []
        else:
            self.shippingDate = shippingDate
        self.shippingDate_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShippingDatesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShippingDatesType.subclass:
            return ShippingDatesType.subclass(*args_, **kwargs_)
        else:
            return ShippingDatesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_shippingDate(self):
        return self.shippingDate
    def set_shippingDate(self, shippingDate):
        self.shippingDate = shippingDate
    def add_shippingDate(self, value):
        self.shippingDate.append(value)
    def insert_shippingDate_at(self, index, value):
        self.shippingDate.insert(index, value)
    def replace_shippingDate_at(self, index, value):
        self.shippingDate[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.shippingDate
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ShippingDatesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShippingDatesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShippingDatesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShippingDatesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShippingDatesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShippingDatesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='ShippingDatesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for shippingDate_ in self.shippingDate:
            namespaceprefix_ = self.shippingDate_nsprefix_ + ':' if (UseCapturedNS_ and self.shippingDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshippingDate>%s</%sshippingDate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(shippingDate_), input_name='shippingDate')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ShippingDatesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for shippingDate_ in self.shippingDate:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}shippingDate').text = self.gds_format_string(shippingDate_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ShippingDatesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('shippingDate=[\n')
        level += 1
        for shippingDate_ in self.shippingDate:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(shippingDate_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'shippingDate':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shippingDate')
            value_ = self.gds_validate_string(value_, node, 'shippingDate')
            self.shippingDate.append(value_)
            self.shippingDate_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.shippingDate[-1])
# end class ShippingDatesType


class SummaryByVatRateType(GeneratedsSuper):
    """SummaryByVatRateType -- Á
    FA m
    é
    rt
    é
    kek szerinti
    ö
    sszes
    í
    t
    é
    s
    Summary according to VAT rates
    vatRate -- Ad
    ó
    m
    é
    rt
    é
    k vagy ad
    ó
    mentess
    é
    g jel
    ö
    l
    é
    se
    Marking the tax rate or the fact of tax exemption
    vatRateNetData -- Adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    nett
    ó
    adatok
    Net data of given tax rate
    vatRateVatData -- Adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    Á
    FA adatok
    VAT data of given tax rate
    vatRateGrossData -- Adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    brutt
    ó
    adatok
    Gross data of given tax rate

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRate=None, vatRateNetData=None, vatRateVatData=None, vatRateGrossData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRate = vatRate
        self.vatRate_nsprefix_ = None
        self.vatRateNetData = vatRateNetData
        self.vatRateNetData_nsprefix_ = None
        self.vatRateVatData = vatRateVatData
        self.vatRateVatData_nsprefix_ = None
        self.vatRateGrossData = vatRateGrossData
        self.vatRateGrossData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummaryByVatRateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummaryByVatRateType.subclass:
            return SummaryByVatRateType.subclass(*args_, **kwargs_)
        else:
            return SummaryByVatRateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRate(self):
        return self.vatRate
    def set_vatRate(self, vatRate):
        self.vatRate = vatRate
    def get_vatRateNetData(self):
        return self.vatRateNetData
    def set_vatRateNetData(self, vatRateNetData):
        self.vatRateNetData = vatRateNetData
    def get_vatRateVatData(self):
        return self.vatRateVatData
    def set_vatRateVatData(self, vatRateVatData):
        self.vatRateVatData = vatRateVatData
    def get_vatRateGrossData(self):
        return self.vatRateGrossData
    def set_vatRateGrossData(self, vatRateGrossData):
        self.vatRateGrossData = vatRateGrossData
    def _hasContent(self):
        if (
            self.vatRate is not None or
            self.vatRateNetData is not None or
            self.vatRateVatData is not None or
            self.vatRateGrossData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='SummaryByVatRateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummaryByVatRateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummaryByVatRateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummaryByVatRateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummaryByVatRateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummaryByVatRateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='SummaryByVatRateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRate is not None:
            namespaceprefix_ = self.vatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRate_nsprefix_) else ''
            self.vatRate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRate', pretty_print=pretty_print)
        if self.vatRateNetData is not None:
            namespaceprefix_ = self.vatRateNetData_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateNetData_nsprefix_) else ''
            self.vatRateNetData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRateNetData', pretty_print=pretty_print)
        if self.vatRateVatData is not None:
            namespaceprefix_ = self.vatRateVatData_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateVatData_nsprefix_) else ''
            self.vatRateVatData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRateVatData', pretty_print=pretty_print)
        if self.vatRateGrossData is not None:
            namespaceprefix_ = self.vatRateGrossData_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateGrossData_nsprefix_) else ''
            self.vatRateGrossData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRateGrossData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SummaryByVatRateType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRate is not None:
            vatRate_ = self.vatRate
            vatRate_.to_etree(element, name_='vatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatRateNetData is not None:
            vatRateNetData_ = self.vatRateNetData
            vatRateNetData_.to_etree(element, name_='vatRateNetData', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatRateVatData is not None:
            vatRateVatData_ = self.vatRateVatData
            vatRateVatData_.to_etree(element, name_='vatRateVatData', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatRateGrossData is not None:
            vatRateGrossData_ = self.vatRateGrossData
            vatRateGrossData_.to_etree(element, name_='vatRateGrossData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummaryByVatRateType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRate is not None:
            showIndent(outfile, level)
            outfile.write('vatRate=model_.VatRateType(\n')
            self.vatRate.exportLiteral(outfile, level, name_='vatRate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatRateNetData is not None:
            showIndent(outfile, level)
            outfile.write('vatRateNetData=model_.VatRateNetDataType(\n')
            self.vatRateNetData.exportLiteral(outfile, level, name_='vatRateNetData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatRateVatData is not None:
            showIndent(outfile, level)
            outfile.write('vatRateVatData=model_.VatRateVatDataType(\n')
            self.vatRateVatData.exportLiteral(outfile, level, name_='vatRateVatData')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatRateGrossData is not None:
            showIndent(outfile, level)
            outfile.write('vatRateGrossData=model_.VatRateGrossDataType(\n')
            self.vatRateGrossData.exportLiteral(outfile, level, name_='vatRateGrossData')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'vatRate':
            obj_ = VatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRate = obj_
            obj_.original_tagname_ = 'vatRate'
        elif nodeName_ == 'vatRateNetData':
            obj_ = VatRateNetDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRateNetData = obj_
            obj_.original_tagname_ = 'vatRateNetData'
        elif nodeName_ == 'vatRateVatData':
            obj_ = VatRateVatDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRateVatData = obj_
            obj_.original_tagname_ = 'vatRateVatData'
        elif nodeName_ == 'vatRateGrossData':
            obj_ = VatRateGrossDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRateGrossData = obj_
            obj_.original_tagname_ = 'vatRateGrossData'
# end class SummaryByVatRateType


class SummaryGrossDataType(GeneratedsSuper):
    """SummaryGrossDataType -- A sz
    á
    mla
    ö
    sszes
    í
    t
    ő
    brutt
    ó
    adatai
    Gross data of the invoice summary
    invoiceGrossAmount -- A sz
    á
    mla brutt
    ó
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben
    Gross amount of the invoice expressed in the currency of the invoice
    invoiceGrossAmountHUF -- A sz
    á
    mla brutt
    ó
    ö
    sszege forintban
    Gross amount of the invoice expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, invoiceGrossAmount=None, invoiceGrossAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.invoiceGrossAmount = invoiceGrossAmount
        self.validate_MonetaryType(self.invoiceGrossAmount)
        self.invoiceGrossAmount_nsprefix_ = "base"
        self.invoiceGrossAmountHUF = invoiceGrossAmountHUF
        self.validate_MonetaryType(self.invoiceGrossAmountHUF)
        self.invoiceGrossAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummaryGrossDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummaryGrossDataType.subclass:
            return SummaryGrossDataType.subclass(*args_, **kwargs_)
        else:
            return SummaryGrossDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_invoiceGrossAmount(self):
        return self.invoiceGrossAmount
    def set_invoiceGrossAmount(self, invoiceGrossAmount):
        self.invoiceGrossAmount = invoiceGrossAmount
    def get_invoiceGrossAmountHUF(self):
        return self.invoiceGrossAmountHUF
    def set_invoiceGrossAmountHUF(self, invoiceGrossAmountHUF):
        self.invoiceGrossAmountHUF = invoiceGrossAmountHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.invoiceGrossAmount is not None or
            self.invoiceGrossAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummaryGrossDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummaryGrossDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummaryGrossDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummaryGrossDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummaryGrossDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummaryGrossDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummaryGrossDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.invoiceGrossAmount is not None:
            namespaceprefix_ = self.invoiceGrossAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceGrossAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceGrossAmount>%s</%sinvoiceGrossAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceGrossAmount, input_name='invoiceGrossAmount'), namespaceprefix_ , eol_))
        if self.invoiceGrossAmountHUF is not None:
            namespaceprefix_ = self.invoiceGrossAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceGrossAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceGrossAmountHUF>%s</%sinvoiceGrossAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceGrossAmountHUF, input_name='invoiceGrossAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SummaryGrossDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.invoiceGrossAmount is not None:
            invoiceGrossAmount_ = self.invoiceGrossAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceGrossAmount').text = self.gds_format_decimal(invoiceGrossAmount_)
        if self.invoiceGrossAmountHUF is not None:
            invoiceGrossAmountHUF_ = self.invoiceGrossAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceGrossAmountHUF').text = self.gds_format_decimal(invoiceGrossAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummaryGrossDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.invoiceGrossAmount is not None:
            showIndent(outfile, level)
            outfile.write('invoiceGrossAmount=%f,\n' % self.invoiceGrossAmount)
        if self.invoiceGrossAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('invoiceGrossAmountHUF=%f,\n' % self.invoiceGrossAmountHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'invoiceGrossAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceGrossAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceGrossAmount')
            self.invoiceGrossAmount = fval_
            self.invoiceGrossAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceGrossAmount)
        elif nodeName_ == 'invoiceGrossAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceGrossAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceGrossAmountHUF')
            self.invoiceGrossAmountHUF = fval_
            self.invoiceGrossAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceGrossAmountHUF)
# end class SummaryGrossDataType


class SummaryNormalType(GeneratedsSuper):
    """SummaryNormalType -- Sz
    á
    mla
    ö
    sszes
    í
    t
    é
    s (nem egyszer
    ű
    s
    í
    tett sz
    á
    mla eset
    é
    n)
    Calculation of invoice totals (not simplified invoice)
    summaryByVatRate -- Ö
    sszes
    í
    t
    é
    s
    Á
    FA-m
    é
    rt
    é
    k szerint
    Calculation of invoice totals per VAT rates
    invoiceNetAmount -- A sz
    á
    mla nett
    ó
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben
    Net amount of the invoice expressed in the currency of the invoice
    invoiceNetAmountHUF -- A sz
    á
    mla nett
    ó
    ö
    sszege forintban
    Net amount of the invoice expressed in HUF
    invoiceVatAmount -- A sz
    á
    mla
    Á
    FA
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben
    VAT amount of the invoice expressed in the currency of the invoice
    invoiceVatAmountHUF -- A sz
    á
    mla
    Á
    FA
    ö
    sszege forintban
    VAT amount of the invoice expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, summaryByVatRate=None, invoiceNetAmount=None, invoiceNetAmountHUF=None, invoiceVatAmount=None, invoiceVatAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if summaryByVatRate is None:
            self.summaryByVatRate = []
        else:
            self.summaryByVatRate = summaryByVatRate
        self.summaryByVatRate_nsprefix_ = None
        self.invoiceNetAmount = invoiceNetAmount
        self.validate_MonetaryType(self.invoiceNetAmount)
        self.invoiceNetAmount_nsprefix_ = "base"
        self.invoiceNetAmountHUF = invoiceNetAmountHUF
        self.validate_MonetaryType(self.invoiceNetAmountHUF)
        self.invoiceNetAmountHUF_nsprefix_ = "base"
        self.invoiceVatAmount = invoiceVatAmount
        self.validate_MonetaryType(self.invoiceVatAmount)
        self.invoiceVatAmount_nsprefix_ = "base"
        self.invoiceVatAmountHUF = invoiceVatAmountHUF
        self.validate_MonetaryType(self.invoiceVatAmountHUF)
        self.invoiceVatAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummaryNormalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummaryNormalType.subclass:
            return SummaryNormalType.subclass(*args_, **kwargs_)
        else:
            return SummaryNormalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_summaryByVatRate(self):
        return self.summaryByVatRate
    def set_summaryByVatRate(self, summaryByVatRate):
        self.summaryByVatRate = summaryByVatRate
    def add_summaryByVatRate(self, value):
        self.summaryByVatRate.append(value)
    def insert_summaryByVatRate_at(self, index, value):
        self.summaryByVatRate.insert(index, value)
    def replace_summaryByVatRate_at(self, index, value):
        self.summaryByVatRate[index] = value
    def get_invoiceNetAmount(self):
        return self.invoiceNetAmount
    def set_invoiceNetAmount(self, invoiceNetAmount):
        self.invoiceNetAmount = invoiceNetAmount
    def get_invoiceNetAmountHUF(self):
        return self.invoiceNetAmountHUF
    def set_invoiceNetAmountHUF(self, invoiceNetAmountHUF):
        self.invoiceNetAmountHUF = invoiceNetAmountHUF
    def get_invoiceVatAmount(self):
        return self.invoiceVatAmount
    def set_invoiceVatAmount(self, invoiceVatAmount):
        self.invoiceVatAmount = invoiceVatAmount
    def get_invoiceVatAmountHUF(self):
        return self.invoiceVatAmountHUF
    def set_invoiceVatAmountHUF(self, invoiceVatAmountHUF):
        self.invoiceVatAmountHUF = invoiceVatAmountHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.summaryByVatRate or
            self.invoiceNetAmount is not None or
            self.invoiceNetAmountHUF is not None or
            self.invoiceVatAmount is not None or
            self.invoiceVatAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummaryNormalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummaryNormalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummaryNormalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummaryNormalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummaryNormalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummaryNormalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummaryNormalType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for summaryByVatRate_ in self.summaryByVatRate:
            namespaceprefix_ = self.summaryByVatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.summaryByVatRate_nsprefix_) else ''
            summaryByVatRate_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='summaryByVatRate', pretty_print=pretty_print)
        if self.invoiceNetAmount is not None:
            namespaceprefix_ = self.invoiceNetAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceNetAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceNetAmount>%s</%sinvoiceNetAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceNetAmount, input_name='invoiceNetAmount'), namespaceprefix_ , eol_))
        if self.invoiceNetAmountHUF is not None:
            namespaceprefix_ = self.invoiceNetAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceNetAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceNetAmountHUF>%s</%sinvoiceNetAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceNetAmountHUF, input_name='invoiceNetAmountHUF'), namespaceprefix_ , eol_))
        if self.invoiceVatAmount is not None:
            namespaceprefix_ = self.invoiceVatAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceVatAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceVatAmount>%s</%sinvoiceVatAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceVatAmount, input_name='invoiceVatAmount'), namespaceprefix_ , eol_))
        if self.invoiceVatAmountHUF is not None:
            namespaceprefix_ = self.invoiceVatAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.invoiceVatAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoiceVatAmountHUF>%s</%sinvoiceVatAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.invoiceVatAmountHUF, input_name='invoiceVatAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SummaryNormalType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for summaryByVatRate_ in self.summaryByVatRate:
            summaryByVatRate_.to_etree(element, name_='summaryByVatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.invoiceNetAmount is not None:
            invoiceNetAmount_ = self.invoiceNetAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceNetAmount').text = self.gds_format_decimal(invoiceNetAmount_)
        if self.invoiceNetAmountHUF is not None:
            invoiceNetAmountHUF_ = self.invoiceNetAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceNetAmountHUF').text = self.gds_format_decimal(invoiceNetAmountHUF_)
        if self.invoiceVatAmount is not None:
            invoiceVatAmount_ = self.invoiceVatAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceVatAmount').text = self.gds_format_decimal(invoiceVatAmount_)
        if self.invoiceVatAmountHUF is not None:
            invoiceVatAmountHUF_ = self.invoiceVatAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}invoiceVatAmountHUF').text = self.gds_format_decimal(invoiceVatAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummaryNormalType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('summaryByVatRate=[\n')
        level += 1
        for summaryByVatRate_ in self.summaryByVatRate:
            showIndent(outfile, level)
            outfile.write('model_.SummaryByVatRateType(\n')
            summaryByVatRate_.exportLiteral(outfile, level, name_='SummaryByVatRateType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.invoiceNetAmount is not None:
            showIndent(outfile, level)
            outfile.write('invoiceNetAmount=%f,\n' % self.invoiceNetAmount)
        if self.invoiceNetAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('invoiceNetAmountHUF=%f,\n' % self.invoiceNetAmountHUF)
        if self.invoiceVatAmount is not None:
            showIndent(outfile, level)
            outfile.write('invoiceVatAmount=%f,\n' % self.invoiceVatAmount)
        if self.invoiceVatAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('invoiceVatAmountHUF=%f,\n' % self.invoiceVatAmountHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'summaryByVatRate':
            obj_ = SummaryByVatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.summaryByVatRate.append(obj_)
            obj_.original_tagname_ = 'summaryByVatRate'
        elif nodeName_ == 'invoiceNetAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceNetAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceNetAmount')
            self.invoiceNetAmount = fval_
            self.invoiceNetAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceNetAmount)
        elif nodeName_ == 'invoiceNetAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceNetAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceNetAmountHUF')
            self.invoiceNetAmountHUF = fval_
            self.invoiceNetAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceNetAmountHUF)
        elif nodeName_ == 'invoiceVatAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceVatAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceVatAmount')
            self.invoiceVatAmount = fval_
            self.invoiceVatAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceVatAmount)
        elif nodeName_ == 'invoiceVatAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'invoiceVatAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'invoiceVatAmountHUF')
            self.invoiceVatAmountHUF = fval_
            self.invoiceVatAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.invoiceVatAmountHUF)
# end class SummaryNormalType


class SummarySimplifiedType(GeneratedsSuper):
    """SummarySimplifiedType -- Egyszer
    ű
    s
    í
    tett sz
    á
    mla
    ö
    sszes
    í
    t
    é
    s
    Calculation of simplified invoice totals
    vatRate -- Ad
    ó
    m
    é
    rt
    é
    k vagy ad
    ó
    mentess
    é
    g jel
    ö
    l
    é
    se
    Marking the tax rate or the fact of tax exemption
    vatContentGrossAmount -- Az adott ad
    ó
    tartalomhoz tartoz
    ó
    é
    rt
    é
    kes
    í
    t
    é
    s vagy szolg
    á
    ltat
    á
    sny
    ú
    jt
    á
    s brutt
    ó
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben
    The gross amount of the sale or service for the given tax amount in the currency of the invoice
    vatContentGrossAmountHUF -- Az adott ad
    ó
    tartalomhoz tartoz
    ó
    é
    rt
    é
    kes
    í
    t
    é
    s vagy szolg
    á
    ltat
    á
    sny
    ú
    jt
    á
    s brutt
    ó
    ö
    sszege forintban
    The gross amount of the sale or service for the given tax amount in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRate=None, vatContentGrossAmount=None, vatContentGrossAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRate = vatRate
        self.vatRate_nsprefix_ = None
        self.vatContentGrossAmount = vatContentGrossAmount
        self.validate_MonetaryType(self.vatContentGrossAmount)
        self.vatContentGrossAmount_nsprefix_ = "base"
        self.vatContentGrossAmountHUF = vatContentGrossAmountHUF
        self.validate_MonetaryType(self.vatContentGrossAmountHUF)
        self.vatContentGrossAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummarySimplifiedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummarySimplifiedType.subclass:
            return SummarySimplifiedType.subclass(*args_, **kwargs_)
        else:
            return SummarySimplifiedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRate(self):
        return self.vatRate
    def set_vatRate(self, vatRate):
        self.vatRate = vatRate
    def get_vatContentGrossAmount(self):
        return self.vatContentGrossAmount
    def set_vatContentGrossAmount(self, vatContentGrossAmount):
        self.vatContentGrossAmount = vatContentGrossAmount
    def get_vatContentGrossAmountHUF(self):
        return self.vatContentGrossAmountHUF
    def set_vatContentGrossAmountHUF(self, vatContentGrossAmountHUF):
        self.vatContentGrossAmountHUF = vatContentGrossAmountHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.vatRate is not None or
            self.vatContentGrossAmount is not None or
            self.vatContentGrossAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummarySimplifiedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummarySimplifiedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummarySimplifiedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummarySimplifiedType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummarySimplifiedType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummarySimplifiedType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='SummarySimplifiedType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRate is not None:
            namespaceprefix_ = self.vatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRate_nsprefix_) else ''
            self.vatRate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatRate', pretty_print=pretty_print)
        if self.vatContentGrossAmount is not None:
            namespaceprefix_ = self.vatContentGrossAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.vatContentGrossAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatContentGrossAmount>%s</%svatContentGrossAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatContentGrossAmount, input_name='vatContentGrossAmount'), namespaceprefix_ , eol_))
        if self.vatContentGrossAmountHUF is not None:
            namespaceprefix_ = self.vatContentGrossAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.vatContentGrossAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatContentGrossAmountHUF>%s</%svatContentGrossAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatContentGrossAmountHUF, input_name='vatContentGrossAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SummarySimplifiedType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRate is not None:
            vatRate_ = self.vatRate
            vatRate_.to_etree(element, name_='vatRate', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatContentGrossAmount is not None:
            vatContentGrossAmount_ = self.vatContentGrossAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatContentGrossAmount').text = self.gds_format_decimal(vatContentGrossAmount_)
        if self.vatContentGrossAmountHUF is not None:
            vatContentGrossAmountHUF_ = self.vatContentGrossAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatContentGrossAmountHUF').text = self.gds_format_decimal(vatContentGrossAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummarySimplifiedType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRate is not None:
            showIndent(outfile, level)
            outfile.write('vatRate=model_.VatRateType(\n')
            self.vatRate.exportLiteral(outfile, level, name_='vatRate')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatContentGrossAmount is not None:
            showIndent(outfile, level)
            outfile.write('vatContentGrossAmount=%f,\n' % self.vatContentGrossAmount)
        if self.vatContentGrossAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('vatContentGrossAmountHUF=%f,\n' % self.vatContentGrossAmountHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'vatRate':
            obj_ = VatRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatRate = obj_
            obj_.original_tagname_ = 'vatRate'
        elif nodeName_ == 'vatContentGrossAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatContentGrossAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatContentGrossAmount')
            self.vatContentGrossAmount = fval_
            self.vatContentGrossAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatContentGrossAmount)
        elif nodeName_ == 'vatContentGrossAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatContentGrossAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatContentGrossAmountHUF')
            self.vatContentGrossAmountHUF = fval_
            self.vatContentGrossAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatContentGrossAmountHUF)
# end class SummarySimplifiedType


class SummaryType(GeneratedsSuper):
    """SummaryType -- Sz
    á
    mla
    ö
    sszes
    í
    t
    é
    s adatai
    Data of calculation of invoice totals
    summaryNormal -- Sz
    á
    mla
    ö
    sszes
    í
    t
    é
    s (nem egyszer
    ű
    s
    í
    tett sz
    á
    mla eset
    é
    n)
    Calculation of invoice totals (not simplified invoice)
    summarySimplified -- Egyszer
    ű
    s
    í
    tett sz
    á
    mla
    ö
    sszes
    í
    t
    é
    s
    Calculation of simplified invoice totals
    summaryGrossData -- A sz
    á
    mla
    ö
    sszes
    í
    t
    ő
    brutt
    ó
    adatai
    Gross data of the invoice summary

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, summaryNormal=None, summarySimplified=None, summaryGrossData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.summaryNormal = summaryNormal
        self.summaryNormal_nsprefix_ = None
        if summarySimplified is None:
            self.summarySimplified = []
        else:
            self.summarySimplified = summarySimplified
        self.summarySimplified_nsprefix_ = None
        self.summaryGrossData = summaryGrossData
        self.summaryGrossData_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SummaryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SummaryType.subclass:
            return SummaryType.subclass(*args_, **kwargs_)
        else:
            return SummaryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_summaryNormal(self):
        return self.summaryNormal
    def set_summaryNormal(self, summaryNormal):
        self.summaryNormal = summaryNormal
    def get_summarySimplified(self):
        return self.summarySimplified
    def set_summarySimplified(self, summarySimplified):
        self.summarySimplified = summarySimplified
    def add_summarySimplified(self, value):
        self.summarySimplified.append(value)
    def insert_summarySimplified_at(self, index, value):
        self.summarySimplified.insert(index, value)
    def replace_summarySimplified_at(self, index, value):
        self.summarySimplified[index] = value
    def get_summaryGrossData(self):
        return self.summaryGrossData
    def set_summaryGrossData(self, summaryGrossData):
        self.summaryGrossData = summaryGrossData
    def _hasContent(self):
        if (
            self.summaryNormal is not None or
            self.summarySimplified or
            self.summaryGrossData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='SummaryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SummaryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SummaryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SummaryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SummaryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SummaryType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='SummaryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.summaryNormal is not None:
            namespaceprefix_ = self.summaryNormal_nsprefix_ + ':' if (UseCapturedNS_ and self.summaryNormal_nsprefix_) else ''
            self.summaryNormal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='summaryNormal', pretty_print=pretty_print)
        for summarySimplified_ in self.summarySimplified:
            namespaceprefix_ = self.summarySimplified_nsprefix_ + ':' if (UseCapturedNS_ and self.summarySimplified_nsprefix_) else ''
            summarySimplified_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='summarySimplified', pretty_print=pretty_print)
        if self.summaryGrossData is not None:
            namespaceprefix_ = self.summaryGrossData_nsprefix_ + ':' if (UseCapturedNS_ and self.summaryGrossData_nsprefix_) else ''
            self.summaryGrossData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='summaryGrossData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='SummaryType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.summaryNormal is not None:
            summaryNormal_ = self.summaryNormal
            summaryNormal_.to_etree(element, name_='summaryNormal', mapping_=mapping_, nsmap_=nsmap_)
        for summarySimplified_ in self.summarySimplified:
            summarySimplified_.to_etree(element, name_='summarySimplified', mapping_=mapping_, nsmap_=nsmap_)
        if self.summaryGrossData is not None:
            summaryGrossData_ = self.summaryGrossData
            summaryGrossData_.to_etree(element, name_='summaryGrossData', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SummaryType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.summaryNormal is not None:
            showIndent(outfile, level)
            outfile.write('summaryNormal=model_.SummaryNormalType(\n')
            self.summaryNormal.exportLiteral(outfile, level, name_='summaryNormal')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('summarySimplified=[\n')
        level += 1
        for summarySimplified_ in self.summarySimplified:
            showIndent(outfile, level)
            outfile.write('model_.SummarySimplifiedType(\n')
            summarySimplified_.exportLiteral(outfile, level, name_='SummarySimplifiedType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.summaryGrossData is not None:
            showIndent(outfile, level)
            outfile.write('summaryGrossData=model_.SummaryGrossDataType(\n')
            self.summaryGrossData.exportLiteral(outfile, level, name_='summaryGrossData')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'summaryNormal':
            obj_ = SummaryNormalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.summaryNormal = obj_
            obj_.original_tagname_ = 'summaryNormal'
        elif nodeName_ == 'summarySimplified':
            obj_ = SummarySimplifiedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.summarySimplified.append(obj_)
            obj_.original_tagname_ = 'summarySimplified'
        elif nodeName_ == 'summaryGrossData':
            obj_ = SummaryGrossDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.summaryGrossData = obj_
            obj_.original_tagname_ = 'summaryGrossData'
# end class SummaryType


class SupplierCompanyCodesType(GeneratedsSuper):
    """SupplierCompanyCodesType -- Az elad
    ó
    v
    á
    llalati k
    ó
    djai
    Company codes of the supplier
    supplierCompanyCode -- Az elad
    ó
    v
    á
    llalati k
    ó
    dja
    Company code of the supplier

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, supplierCompanyCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if supplierCompanyCode is None:
            self.supplierCompanyCode = []
        else:
            self.supplierCompanyCode = supplierCompanyCode
        self.supplierCompanyCode_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SupplierCompanyCodesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SupplierCompanyCodesType.subclass:
            return SupplierCompanyCodesType.subclass(*args_, **kwargs_)
        else:
            return SupplierCompanyCodesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_supplierCompanyCode(self):
        return self.supplierCompanyCode
    def set_supplierCompanyCode(self, supplierCompanyCode):
        self.supplierCompanyCode = supplierCompanyCode
    def add_supplierCompanyCode(self, value):
        self.supplierCompanyCode.append(value)
    def insert_supplierCompanyCode_at(self, index, value):
        self.supplierCompanyCode.insert(index, value)
    def replace_supplierCompanyCode_at(self, index, value):
        self.supplierCompanyCode[index] = value
    def validate_SimpleText100NotBlankType(self, value):
        result = True
        # Validate type SimpleText100NotBlankType, a restriction on AtomicStringType100.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText100NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText100NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText100NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText100NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText100NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.supplierCompanyCode
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='SupplierCompanyCodesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SupplierCompanyCodesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SupplierCompanyCodesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SupplierCompanyCodesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SupplierCompanyCodesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SupplierCompanyCodesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='SupplierCompanyCodesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for supplierCompanyCode_ in self.supplierCompanyCode:
            namespaceprefix_ = self.supplierCompanyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierCompanyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierCompanyCode>%s</%ssupplierCompanyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(supplierCompanyCode_), input_name='supplierCompanyCode')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SupplierCompanyCodesType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        for supplierCompanyCode_ in self.supplierCompanyCode:
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}supplierCompanyCode').text = self.gds_format_string(supplierCompanyCode_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SupplierCompanyCodesType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('supplierCompanyCode=[\n')
        level += 1
        for supplierCompanyCode_ in self.supplierCompanyCode:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(supplierCompanyCode_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'supplierCompanyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierCompanyCode')
            value_ = self.gds_validate_string(value_, node, 'supplierCompanyCode')
            self.supplierCompanyCode.append(value_)
            self.supplierCompanyCode_nsprefix_ = child_.prefix
            # validate type SimpleText100NotBlankType
            self.validate_SimpleText100NotBlankType(self.supplierCompanyCode[-1])
# end class SupplierCompanyCodesType


class SupplierInfoType(GeneratedsSuper):
    """SupplierInfoType -- A sz
    á
    ll
    í
    t
    ó
    (elad
    ó
    ) adatai
    Invoice supplier (seller) data
    supplierTaxNumber -- Belf
    ö
    ldi ad
    ó
    sz
    á
    m vagy csoportazonos
    í
    t
    ó
    sz
    á
    m
    Tax number or group identification number
    groupMemberTaxNumber -- Csoport tag ad
    ó
    sz
    á
    ma, ha a term
    é
    kbeszerz
    é
    s vagy szolg
    á
    ltat
    á
    s ny
    ú
    jt
    á
    sa csoportazonos
    í
    t
    ó
    sz
    á
    m alatt t
    ö
    rt
    é
    nt
    Tax number of group member, when the supply of goods or services is done under group identification number
    communityVatNumber -- K
    ö
    z
    ö
    ss
    é
    gi ad
    ó
    sz
    á
    m
    Community tax number
    supplierName -- Az elad
    ó
    (sz
    á
    ll
    í
    t
    ó
    ) neve
    Name of the seller (supplier)
    supplierAddress -- Az elad
    ó
    (sz
    á
    ll
    í
    t
    ó
    ) c
    í
    me
    Address of the seller (supplier)
    supplierBankAccountNumber -- Az elad
    ó
    (sz
    á
    ll
    í
    t
    ó
    ) banksz
    á
    mlasz
    á
    ma
    Bank account number of the seller (supplier)
    individualExemption -- É
    rt
    é
    ke true, amennyiben az elad
    ó
    (sz
    á
    ll
    í
    t
    ó
    ) alanyi
    Á
    FA mentes
    Value is true if the seller (supplier) is individually exempted from VAT
    exciseLicenceNum -- Az elad
    ó
    ad
    ó
    rakt
    á
    ri enged
    é
    ly
    é
    nek vagy j
    ö
    ved
    é
    ki enged
    é
    ly
    é
    nek sz
    á
    ma (2016.
    é
    vi LXVIII. tv.)
    Number of supplier
    ’
    s tax warehouse license or excise license (Act LXVIII of 2016)

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, supplierTaxNumber=None, groupMemberTaxNumber=None, communityVatNumber=None, supplierName=None, supplierAddress=None, supplierBankAccountNumber=None, individualExemption=None, exciseLicenceNum=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.supplierTaxNumber = supplierTaxNumber
        self.supplierTaxNumber_nsprefix_ = "base"
        self.groupMemberTaxNumber = groupMemberTaxNumber
        self.groupMemberTaxNumber_nsprefix_ = "base"
        self.communityVatNumber = communityVatNumber
        self.validate_CommunityVatNumberType(self.communityVatNumber)
        self.communityVatNumber_nsprefix_ = "common"
        self.supplierName = supplierName
        self.validate_SimpleText512NotBlankType(self.supplierName)
        self.supplierName_nsprefix_ = "common"
        self.supplierAddress = supplierAddress
        self.supplierAddress_nsprefix_ = "base"
        self.supplierBankAccountNumber = supplierBankAccountNumber
        self.validate_BankAccountNumberType(self.supplierBankAccountNumber)
        self.supplierBankAccountNumber_nsprefix_ = "common"
        self.individualExemption = individualExemption
        self.individualExemption_nsprefix_ = "xs"
        self.exciseLicenceNum = exciseLicenceNum
        self.validate_SimpleText50NotBlankType(self.exciseLicenceNum)
        self.exciseLicenceNum_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SupplierInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SupplierInfoType.subclass:
            return SupplierInfoType.subclass(*args_, **kwargs_)
        else:
            return SupplierInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_supplierTaxNumber(self):
        return self.supplierTaxNumber
    def set_supplierTaxNumber(self, supplierTaxNumber):
        self.supplierTaxNumber = supplierTaxNumber
    def get_groupMemberTaxNumber(self):
        return self.groupMemberTaxNumber
    def set_groupMemberTaxNumber(self, groupMemberTaxNumber):
        self.groupMemberTaxNumber = groupMemberTaxNumber
    def get_communityVatNumber(self):
        return self.communityVatNumber
    def set_communityVatNumber(self, communityVatNumber):
        self.communityVatNumber = communityVatNumber
    def get_supplierName(self):
        return self.supplierName
    def set_supplierName(self, supplierName):
        self.supplierName = supplierName
    def get_supplierAddress(self):
        return self.supplierAddress
    def set_supplierAddress(self, supplierAddress):
        self.supplierAddress = supplierAddress
    def get_supplierBankAccountNumber(self):
        return self.supplierBankAccountNumber
    def set_supplierBankAccountNumber(self, supplierBankAccountNumber):
        self.supplierBankAccountNumber = supplierBankAccountNumber
    def get_individualExemption(self):
        return self.individualExemption
    def set_individualExemption(self, individualExemption):
        self.individualExemption = individualExemption
    def get_exciseLicenceNum(self):
        return self.exciseLicenceNum
    def set_exciseLicenceNum(self, exciseLicenceNum):
        self.exciseLicenceNum = exciseLicenceNum
    def validate_CommunityVatNumberType(self, value):
        result = True
        # Validate type CommunityVatNumberType, a restriction on AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CommunityVatNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CommunityVatNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CommunityVatNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CommunityVatNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CommunityVatNumberType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CommunityVatNumberType_patterns_, ))
                result = False
        return result
    validate_CommunityVatNumberType_patterns_ = [['^([A-Z]{2}[0-9A-Z]{2,13})$']]
    def validate_SimpleText512NotBlankType(self, value):
        result = True
        # Validate type SimpleText512NotBlankType, a restriction on AtomicStringType512.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText512NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText512NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText512NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText512NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText512NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_BankAccountNumberType(self, value):
        result = True
        # Validate type BankAccountNumberType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 34:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on BankAccountNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on BankAccountNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on BankAccountNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on BankAccountNumberType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_BankAccountNumberType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_BankAccountNumberType_patterns_, ))
                result = False
        return result
    validate_BankAccountNumberType_patterns_ = [['^([0-9]{8}[-][0-9]{8}[-][0-9]{8}|[0-9]{8}[-][0-9]{8}|[A-Z]{2}[0-9]{2}[0-9A-Za-z]{11,30})$']]
    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.supplierTaxNumber is not None or
            self.groupMemberTaxNumber is not None or
            self.communityVatNumber is not None or
            self.supplierName is not None or
            self.supplierAddress is not None or
            self.supplierBankAccountNumber is not None or
            self.individualExemption is not None or
            self.exciseLicenceNum is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='SupplierInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SupplierInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SupplierInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SupplierInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SupplierInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SupplierInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='SupplierInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.supplierTaxNumber is not None:
            namespaceprefix_ = self.supplierTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierTaxNumber_nsprefix_) else ''
            self.supplierTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='supplierTaxNumber', pretty_print=pretty_print)
        if self.groupMemberTaxNumber is not None:
            namespaceprefix_ = self.groupMemberTaxNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.groupMemberTaxNumber_nsprefix_) else ''
            self.groupMemberTaxNumber.export(outfile, level, namespaceprefix_, namespacedef_='', name_='groupMemberTaxNumber', pretty_print=pretty_print)
        if self.communityVatNumber is not None:
            namespaceprefix_ = self.communityVatNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.communityVatNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scommunityVatNumber>%s</%scommunityVatNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.communityVatNumber), input_name='communityVatNumber')), namespaceprefix_ , eol_))
        if self.supplierName is not None:
            namespaceprefix_ = self.supplierName_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierName>%s</%ssupplierName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.supplierName), input_name='supplierName')), namespaceprefix_ , eol_))
        if self.supplierAddress is not None:
            namespaceprefix_ = self.supplierAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierAddress_nsprefix_) else ''
            self.supplierAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='supplierAddress', pretty_print=pretty_print)
        if self.supplierBankAccountNumber is not None:
            namespaceprefix_ = self.supplierBankAccountNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.supplierBankAccountNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplierBankAccountNumber>%s</%ssupplierBankAccountNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.supplierBankAccountNumber), input_name='supplierBankAccountNumber')), namespaceprefix_ , eol_))
        if self.individualExemption is not None:
            namespaceprefix_ = self.individualExemption_nsprefix_ + ':' if (UseCapturedNS_ and self.individualExemption_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindividualExemption>%s</%sindividualExemption>%s' % (namespaceprefix_ , self.gds_format_boolean(self.individualExemption, input_name='individualExemption'), namespaceprefix_ , eol_))
        if self.exciseLicenceNum is not None:
            namespaceprefix_ = self.exciseLicenceNum_nsprefix_ + ':' if (UseCapturedNS_ and self.exciseLicenceNum_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexciseLicenceNum>%s</%sexciseLicenceNum>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.exciseLicenceNum), input_name='exciseLicenceNum')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='SupplierInfoType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.supplierTaxNumber is not None:
            supplierTaxNumber_ = self.supplierTaxNumber
            supplierTaxNumber_.to_etree(element, name_='supplierTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if self.groupMemberTaxNumber is not None:
            groupMemberTaxNumber_ = self.groupMemberTaxNumber
            groupMemberTaxNumber_.to_etree(element, name_='groupMemberTaxNumber', mapping_=mapping_, nsmap_=nsmap_)
        if self.communityVatNumber is not None:
            communityVatNumber_ = self.communityVatNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}communityVatNumber').text = self.gds_format_string(communityVatNumber_)
        if self.supplierName is not None:
            supplierName_ = self.supplierName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}supplierName').text = self.gds_format_string(supplierName_)
        if self.supplierAddress is not None:
            supplierAddress_ = self.supplierAddress
            supplierAddress_.to_etree(element, name_='supplierAddress', mapping_=mapping_, nsmap_=nsmap_)
        if self.supplierBankAccountNumber is not None:
            supplierBankAccountNumber_ = self.supplierBankAccountNumber
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}supplierBankAccountNumber').text = self.gds_format_string(supplierBankAccountNumber_)
        if self.individualExemption is not None:
            individualExemption_ = self.individualExemption
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}individualExemption').text = self.gds_format_boolean(individualExemption_)
        if self.exciseLicenceNum is not None:
            exciseLicenceNum_ = self.exciseLicenceNum
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}exciseLicenceNum').text = self.gds_format_string(exciseLicenceNum_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='SupplierInfoType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.supplierTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('supplierTaxNumber=model_.TaxNumberType(\n')
            self.supplierTaxNumber.exportLiteral(outfile, level, name_='supplierTaxNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.groupMemberTaxNumber is not None:
            showIndent(outfile, level)
            outfile.write('groupMemberTaxNumber=model_.TaxNumberType(\n')
            self.groupMemberTaxNumber.exportLiteral(outfile, level, name_='groupMemberTaxNumber')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.communityVatNumber is not None:
            showIndent(outfile, level)
            outfile.write('communityVatNumber=%s,\n' % self.gds_encode(quote_python(self.communityVatNumber)))
        if self.supplierName is not None:
            showIndent(outfile, level)
            outfile.write('supplierName=%s,\n' % self.gds_encode(quote_python(self.supplierName)))
        if self.supplierAddress is not None:
            showIndent(outfile, level)
            outfile.write('supplierAddress=model_.AddressType(\n')
            self.supplierAddress.exportLiteral(outfile, level, name_='supplierAddress')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.supplierBankAccountNumber is not None:
            showIndent(outfile, level)
            outfile.write('supplierBankAccountNumber=%s,\n' % self.gds_encode(quote_python(self.supplierBankAccountNumber)))
        if self.individualExemption is not None:
            showIndent(outfile, level)
            outfile.write('individualExemption=%s,\n' % self.individualExemption)
        if self.exciseLicenceNum is not None:
            showIndent(outfile, level)
            outfile.write('exciseLicenceNum=%s,\n' % self.gds_encode(quote_python(self.exciseLicenceNum)))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'supplierTaxNumber':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplierTaxNumber = obj_
            obj_.original_tagname_ = 'supplierTaxNumber'
        elif nodeName_ == 'groupMemberTaxNumber':
            class_obj_ = self.get_class_obj_(child_, TaxNumberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.groupMemberTaxNumber = obj_
            obj_.original_tagname_ = 'groupMemberTaxNumber'
        elif nodeName_ == 'communityVatNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'communityVatNumber')
            value_ = self.gds_validate_string(value_, node, 'communityVatNumber')
            self.communityVatNumber = value_
            self.communityVatNumber_nsprefix_ = child_.prefix
            # validate type CommunityVatNumberType
            self.validate_CommunityVatNumberType(self.communityVatNumber)
        elif nodeName_ == 'supplierName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierName')
            value_ = self.gds_validate_string(value_, node, 'supplierName')
            self.supplierName = value_
            self.supplierName_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.supplierName)
        elif nodeName_ == 'supplierAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplierAddress = obj_
            obj_.original_tagname_ = 'supplierAddress'
        elif nodeName_ == 'supplierBankAccountNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplierBankAccountNumber')
            value_ = self.gds_validate_string(value_, node, 'supplierBankAccountNumber')
            self.supplierBankAccountNumber = value_
            self.supplierBankAccountNumber_nsprefix_ = child_.prefix
            # validate type BankAccountNumberType
            self.validate_BankAccountNumberType(self.supplierBankAccountNumber)
        elif nodeName_ == 'individualExemption':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'individualExemption')
            ival_ = self.gds_validate_boolean(ival_, node, 'individualExemption')
            self.individualExemption = ival_
            self.individualExemption_nsprefix_ = child_.prefix
        elif nodeName_ == 'exciseLicenceNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'exciseLicenceNum')
            value_ = self.gds_validate_string(value_, node, 'exciseLicenceNum')
            self.exciseLicenceNum = value_
            self.exciseLicenceNum_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.exciseLicenceNum)
# end class SupplierInfoType


class VatAmountMismatchType(GeneratedsSuper):
    """VatAmountMismatchType -- Ad
    ó
    alap
    é
    s felsz
    á
    m
    í
    tott ad
    ó
    elt
    é
    r
    é
    s
    é
    nek adatai
    Data of mismatching tax base and levied tax
    vatRate -- Ad
    ó
    m
    é
    rt
    é
    k, ad
    ó
    tartalom
    VAT rate, VAT content
    case -- Az eset le
    í
    r
    á
    sa k
    ó
    ddal
    Case notation with code

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRate=None, case=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRate = vatRate
        self.validate_RateType(self.vatRate)
        self.vatRate_nsprefix_ = None
        self.case = case
        self.validate_SimpleText50NotBlankType(self.case)
        self.case_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatAmountMismatchType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatAmountMismatchType.subclass:
            return VatAmountMismatchType.subclass(*args_, **kwargs_)
        else:
            return VatAmountMismatchType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRate(self):
        return self.vatRate
    def set_vatRate(self, vatRate):
        self.vatRate = vatRate
    def get_case(self):
        return self.case
    def set_case(self, case):
        self.case = case
    def validate_RateType(self, value):
        result = True
        # Validate type RateType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_SimpleText50NotBlankType(self, value):
        result = True
        # Validate type SimpleText50NotBlankType, a restriction on AtomicStringType50.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText50NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText50NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText50NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText50NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText50NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.vatRate is not None or
            self.case is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='VatAmountMismatchType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatAmountMismatchType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatAmountMismatchType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatAmountMismatchType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatAmountMismatchType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatAmountMismatchType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='VatAmountMismatchType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRate is not None:
            namespaceprefix_ = self.vatRate_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRate>%s</%svatRate>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRate, input_name='vatRate'), namespaceprefix_ , eol_))
        if self.case is not None:
            namespaceprefix_ = self.case_nsprefix_ + ':' if (UseCapturedNS_ and self.case_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scase>%s</%scase>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.case), input_name='case')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatAmountMismatchType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRate is not None:
            vatRate_ = self.vatRate
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRate').text = self.gds_format_decimal(vatRate_)
        if self.case is not None:
            case_ = self.case
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}case').text = self.gds_format_string(case_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatAmountMismatchType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRate is not None:
            showIndent(outfile, level)
            outfile.write('vatRate=%f,\n' % self.vatRate)
        if self.case is not None:
            showIndent(outfile, level)
            outfile.write('case=%s,\n' % self.gds_encode(quote_python(self.case)))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'vatRate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRate')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRate')
            self.vatRate = fval_
            self.vatRate_nsprefix_ = child_.prefix
            # validate type RateType
            self.validate_RateType(self.vatRate)
        elif nodeName_ == 'case':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'case')
            value_ = self.gds_validate_string(value_, node, 'case')
            self.case = value_
            self.case_nsprefix_ = child_.prefix
            # validate type SimpleText50NotBlankType
            self.validate_SimpleText50NotBlankType(self.case)
# end class VatAmountMismatchType


class VatRateGrossDataType(GeneratedsSuper):
    """VatRateGrossDataType -- Adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    brutt
    ó
    adatok
    Gross data of given tax rate
    vatRateGrossAmount -- Az adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    é
    rt
    é
    kes
    í
    t
    é
    s vagy szolg
    á
    ltat
    á
    sny
    ú
    jt
    á
    s brutt
    ó
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben
    Gross amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    vatRateGrossAmountHUF -- Az adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    é
    rt
    é
    kes
    í
    t
    é
    s vagy szolg
    á
    ltat
    á
    sny
    ú
    jt
    á
    s brutt
    ó
    ö
    sszege forintban
    Gross amount of sales or service delivery under a given tax rate expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRateGrossAmount=None, vatRateGrossAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRateGrossAmount = vatRateGrossAmount
        self.validate_MonetaryType(self.vatRateGrossAmount)
        self.vatRateGrossAmount_nsprefix_ = "base"
        self.vatRateGrossAmountHUF = vatRateGrossAmountHUF
        self.validate_MonetaryType(self.vatRateGrossAmountHUF)
        self.vatRateGrossAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatRateGrossDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatRateGrossDataType.subclass:
            return VatRateGrossDataType.subclass(*args_, **kwargs_)
        else:
            return VatRateGrossDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRateGrossAmount(self):
        return self.vatRateGrossAmount
    def set_vatRateGrossAmount(self, vatRateGrossAmount):
        self.vatRateGrossAmount = vatRateGrossAmount
    def get_vatRateGrossAmountHUF(self):
        return self.vatRateGrossAmountHUF
    def set_vatRateGrossAmountHUF(self, vatRateGrossAmountHUF):
        self.vatRateGrossAmountHUF = vatRateGrossAmountHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.vatRateGrossAmount is not None or
            self.vatRateGrossAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateGrossDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatRateGrossDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatRateGrossDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatRateGrossDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatRateGrossDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatRateGrossDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateGrossDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRateGrossAmount is not None:
            namespaceprefix_ = self.vatRateGrossAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateGrossAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateGrossAmount>%s</%svatRateGrossAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateGrossAmount, input_name='vatRateGrossAmount'), namespaceprefix_ , eol_))
        if self.vatRateGrossAmountHUF is not None:
            namespaceprefix_ = self.vatRateGrossAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateGrossAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateGrossAmountHUF>%s</%svatRateGrossAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateGrossAmountHUF, input_name='vatRateGrossAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatRateGrossDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRateGrossAmount is not None:
            vatRateGrossAmount_ = self.vatRateGrossAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateGrossAmount').text = self.gds_format_decimal(vatRateGrossAmount_)
        if self.vatRateGrossAmountHUF is not None:
            vatRateGrossAmountHUF_ = self.vatRateGrossAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateGrossAmountHUF').text = self.gds_format_decimal(vatRateGrossAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatRateGrossDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRateGrossAmount is not None:
            showIndent(outfile, level)
            outfile.write('vatRateGrossAmount=%f,\n' % self.vatRateGrossAmount)
        if self.vatRateGrossAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('vatRateGrossAmountHUF=%f,\n' % self.vatRateGrossAmountHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'vatRateGrossAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateGrossAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateGrossAmount')
            self.vatRateGrossAmount = fval_
            self.vatRateGrossAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateGrossAmount)
        elif nodeName_ == 'vatRateGrossAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateGrossAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateGrossAmountHUF')
            self.vatRateGrossAmountHUF = fval_
            self.vatRateGrossAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateGrossAmountHUF)
# end class VatRateGrossDataType


class VatRateNetDataType(GeneratedsSuper):
    """VatRateNetDataType -- Adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    nett
    ó
    adatok
    Net data of given tax rate
    vatRateNetAmount -- Az adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    é
    rt
    é
    kes
    í
    t
    é
    s vagy szolg
    á
    ltat
    á
    sny
    ú
    jt
    á
    s nett
    ó
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben
    Net amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    vatRateNetAmountHUF -- Az adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    é
    rt
    é
    kes
    í
    t
    é
    s vagy szolg
    á
    ltat
    á
    sny
    ú
    jt
    á
    s nett
    ó
    ö
    sszege forintban
    Net amount of sales or service delivery under a given tax rate expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRateNetAmount=None, vatRateNetAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRateNetAmount = vatRateNetAmount
        self.validate_MonetaryType(self.vatRateNetAmount)
        self.vatRateNetAmount_nsprefix_ = "base"
        self.vatRateNetAmountHUF = vatRateNetAmountHUF
        self.validate_MonetaryType(self.vatRateNetAmountHUF)
        self.vatRateNetAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatRateNetDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatRateNetDataType.subclass:
            return VatRateNetDataType.subclass(*args_, **kwargs_)
        else:
            return VatRateNetDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRateNetAmount(self):
        return self.vatRateNetAmount
    def set_vatRateNetAmount(self, vatRateNetAmount):
        self.vatRateNetAmount = vatRateNetAmount
    def get_vatRateNetAmountHUF(self):
        return self.vatRateNetAmountHUF
    def set_vatRateNetAmountHUF(self, vatRateNetAmountHUF):
        self.vatRateNetAmountHUF = vatRateNetAmountHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.vatRateNetAmount is not None or
            self.vatRateNetAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateNetDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatRateNetDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatRateNetDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatRateNetDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatRateNetDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatRateNetDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateNetDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRateNetAmount is not None:
            namespaceprefix_ = self.vatRateNetAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateNetAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateNetAmount>%s</%svatRateNetAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateNetAmount, input_name='vatRateNetAmount'), namespaceprefix_ , eol_))
        if self.vatRateNetAmountHUF is not None:
            namespaceprefix_ = self.vatRateNetAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateNetAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateNetAmountHUF>%s</%svatRateNetAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateNetAmountHUF, input_name='vatRateNetAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatRateNetDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRateNetAmount is not None:
            vatRateNetAmount_ = self.vatRateNetAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateNetAmount').text = self.gds_format_decimal(vatRateNetAmount_)
        if self.vatRateNetAmountHUF is not None:
            vatRateNetAmountHUF_ = self.vatRateNetAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateNetAmountHUF').text = self.gds_format_decimal(vatRateNetAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatRateNetDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRateNetAmount is not None:
            showIndent(outfile, level)
            outfile.write('vatRateNetAmount=%f,\n' % self.vatRateNetAmount)
        if self.vatRateNetAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('vatRateNetAmountHUF=%f,\n' % self.vatRateNetAmountHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'vatRateNetAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateNetAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateNetAmount')
            self.vatRateNetAmount = fval_
            self.vatRateNetAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateNetAmount)
        elif nodeName_ == 'vatRateNetAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateNetAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateNetAmountHUF')
            self.vatRateNetAmountHUF = fval_
            self.vatRateNetAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateNetAmountHUF)
# end class VatRateNetDataType


class VatRateType(GeneratedsSuper):
    """VatRateType -- Az ad
    ó
    m
    é
    rt
    é
    k vagy az ad
    ó
    mentes
    é
    rt
    é
    kes
    í
    t
    é
    s jel
    ö
    l
    é
    se
    Marking tax rate or tax exempt supply
    vatPercentage -- Az alkalmazott ad
    ó
    m
    é
    rt
    é
    ke -
    Á
    FA tv. 169.
    §
    j)
    Applied tax rate - section 169 (j) of the VAT law
    vatContent -- Á
    FA tartalom egyszer
    ű
    s
    í
    tett sz
    á
    mla eset
    é
    n
    VAT content in case of simplified invoice
    vatExemption -- Az ad
    ó
    mentess
    é
    g jel
    ö
    l
    é
    se -
    Á
    FA tv. 169.
    §
    m)
    Marking tax exemption -  section 169 (m) of the VAT law
    vatOutOfScope -- Az
    Á
    FA t
    ö
    rv
    é
    ny hat
    á
    ly
    á
    n k
    í
    v
    ü
    li
    Out of scope of the VAT law
    vatDomesticReverseCharge -- A belf
    ö
    ldi ford
    í
    tott ad
    ó
    z
    á
    s jel
    ö
    l
    é
    se -
    Á
    FA tv. 142.
    §
    Marking the national is reverse charge taxation - section 142 of the VAT law
    marginSchemeIndicator -- K
    ü
    l
    ö
    nb
    ö
    zet szerinti szab
    á
    lyoz
    á
    s jel
    ö
    l
    é
    se -
    Á
    FA tv. 169.
    §
    p) q)
    Marking the margin-scheme taxation as per section 169 (p)(q)
    vatAmountMismatch -- Ad
    ó
    alap
    é
    s felsz
    á
    m
    í
    tott ad
    ó
    elt
    é
    r
    é
    s
    é
    nek esetei
    Different cases of mismatching tax base and levied tax
    noVatCharge -- Nincs felsz
    á
    m
    í
    tott
    á
    fa a 17.
    §
    alapj
    á
    n
    No VAT charged under Section 17

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatPercentage=None, vatContent=None, vatExemption=None, vatOutOfScope=None, vatDomesticReverseCharge=None, marginSchemeIndicator=None, vatAmountMismatch=None, noVatCharge=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatPercentage = vatPercentage
        self.validate_RateType(self.vatPercentage)
        self.vatPercentage_nsprefix_ = None
        self.vatContent = vatContent
        self.validate_RateType(self.vatContent)
        self.vatContent_nsprefix_ = None
        self.vatExemption = vatExemption
        self.vatExemption_nsprefix_ = None
        self.vatOutOfScope = vatOutOfScope
        self.vatOutOfScope_nsprefix_ = None
        self.vatDomesticReverseCharge = vatDomesticReverseCharge
        self.vatDomesticReverseCharge_nsprefix_ = "xs"
        self.marginSchemeIndicator = marginSchemeIndicator
        self.validate_MarginSchemeType(self.marginSchemeIndicator)
        self.marginSchemeIndicator_nsprefix_ = None
        self.vatAmountMismatch = vatAmountMismatch
        self.vatAmountMismatch_nsprefix_ = None
        self.noVatCharge = noVatCharge
        self.noVatCharge_nsprefix_ = "xs"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatRateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatRateType.subclass:
            return VatRateType.subclass(*args_, **kwargs_)
        else:
            return VatRateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatPercentage(self):
        return self.vatPercentage
    def set_vatPercentage(self, vatPercentage):
        self.vatPercentage = vatPercentage
    def get_vatContent(self):
        return self.vatContent
    def set_vatContent(self, vatContent):
        self.vatContent = vatContent
    def get_vatExemption(self):
        return self.vatExemption
    def set_vatExemption(self, vatExemption):
        self.vatExemption = vatExemption
    def get_vatOutOfScope(self):
        return self.vatOutOfScope
    def set_vatOutOfScope(self, vatOutOfScope):
        self.vatOutOfScope = vatOutOfScope
    def get_vatDomesticReverseCharge(self):
        return self.vatDomesticReverseCharge
    def set_vatDomesticReverseCharge(self, vatDomesticReverseCharge):
        self.vatDomesticReverseCharge = vatDomesticReverseCharge
    def get_marginSchemeIndicator(self):
        return self.marginSchemeIndicator
    def set_marginSchemeIndicator(self, marginSchemeIndicator):
        self.marginSchemeIndicator = marginSchemeIndicator
    def get_vatAmountMismatch(self):
        return self.vatAmountMismatch
    def set_vatAmountMismatch(self, vatAmountMismatch):
        self.vatAmountMismatch = vatAmountMismatch
    def get_noVatCharge(self):
        return self.noVatCharge
    def set_noVatCharge(self, noVatCharge):
        self.noVatCharge = noVatCharge
    def validate_RateType(self, value):
        result = True
        # Validate type RateType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on RateType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_MarginSchemeType(self, value):
        result = True
        # Validate type MarginSchemeType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['TRAVEL_AGENCY', 'SECOND_HAND', 'ARTWORK', 'ANTIQUES']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on MarginSchemeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on MarginSchemeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on MarginSchemeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.vatPercentage is not None or
            self.vatContent is not None or
            self.vatExemption is not None or
            self.vatOutOfScope is not None or
            self.vatDomesticReverseCharge is not None or
            self.marginSchemeIndicator is not None or
            self.vatAmountMismatch is not None or
            self.noVatCharge is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='VatRateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatRateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatRateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatRateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatRateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatRateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='VatRateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatPercentage is not None:
            namespaceprefix_ = self.vatPercentage_nsprefix_ + ':' if (UseCapturedNS_ and self.vatPercentage_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatPercentage>%s</%svatPercentage>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatPercentage, input_name='vatPercentage'), namespaceprefix_ , eol_))
        if self.vatContent is not None:
            namespaceprefix_ = self.vatContent_nsprefix_ + ':' if (UseCapturedNS_ and self.vatContent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatContent>%s</%svatContent>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatContent, input_name='vatContent'), namespaceprefix_ , eol_))
        if self.vatExemption is not None:
            namespaceprefix_ = self.vatExemption_nsprefix_ + ':' if (UseCapturedNS_ and self.vatExemption_nsprefix_) else ''
            self.vatExemption.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatExemption', pretty_print=pretty_print)
        if self.vatOutOfScope is not None:
            namespaceprefix_ = self.vatOutOfScope_nsprefix_ + ':' if (UseCapturedNS_ and self.vatOutOfScope_nsprefix_) else ''
            self.vatOutOfScope.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatOutOfScope', pretty_print=pretty_print)
        if self.vatDomesticReverseCharge is not None:
            namespaceprefix_ = self.vatDomesticReverseCharge_nsprefix_ + ':' if (UseCapturedNS_ and self.vatDomesticReverseCharge_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatDomesticReverseCharge>%s</%svatDomesticReverseCharge>%s' % (namespaceprefix_ , self.gds_format_boolean(self.vatDomesticReverseCharge, input_name='vatDomesticReverseCharge'), namespaceprefix_ , eol_))
        if self.marginSchemeIndicator is not None:
            namespaceprefix_ = self.marginSchemeIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.marginSchemeIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smarginSchemeIndicator>%s</%smarginSchemeIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.marginSchemeIndicator), input_name='marginSchemeIndicator')), namespaceprefix_ , eol_))
        if self.vatAmountMismatch is not None:
            namespaceprefix_ = self.vatAmountMismatch_nsprefix_ + ':' if (UseCapturedNS_ and self.vatAmountMismatch_nsprefix_) else ''
            self.vatAmountMismatch.export(outfile, level, namespaceprefix_, namespacedef_='', name_='vatAmountMismatch', pretty_print=pretty_print)
        if self.noVatCharge is not None:
            namespaceprefix_ = self.noVatCharge_nsprefix_ + ':' if (UseCapturedNS_ and self.noVatCharge_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snoVatCharge>%s</%snoVatCharge>%s' % (namespaceprefix_ , self.gds_format_boolean(self.noVatCharge, input_name='noVatCharge'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatRateType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatPercentage is not None:
            vatPercentage_ = self.vatPercentage
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatPercentage').text = self.gds_format_decimal(vatPercentage_)
        if self.vatContent is not None:
            vatContent_ = self.vatContent
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatContent').text = self.gds_format_decimal(vatContent_)
        if self.vatExemption is not None:
            vatExemption_ = self.vatExemption
            vatExemption_.to_etree(element, name_='vatExemption', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatOutOfScope is not None:
            vatOutOfScope_ = self.vatOutOfScope
            vatOutOfScope_.to_etree(element, name_='vatOutOfScope', mapping_=mapping_, nsmap_=nsmap_)
        if self.vatDomesticReverseCharge is not None:
            vatDomesticReverseCharge_ = self.vatDomesticReverseCharge
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatDomesticReverseCharge').text = self.gds_format_boolean(vatDomesticReverseCharge_)
        if self.marginSchemeIndicator is not None:
            marginSchemeIndicator_ = self.marginSchemeIndicator
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}marginSchemeIndicator').text = self.gds_format_string(marginSchemeIndicator_)
        if self.vatAmountMismatch is not None:
            vatAmountMismatch_ = self.vatAmountMismatch
            vatAmountMismatch_.to_etree(element, name_='vatAmountMismatch', mapping_=mapping_, nsmap_=nsmap_)
        if self.noVatCharge is not None:
            noVatCharge_ = self.noVatCharge
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}noVatCharge').text = self.gds_format_boolean(noVatCharge_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatRateType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatPercentage is not None:
            showIndent(outfile, level)
            outfile.write('vatPercentage=%f,\n' % self.vatPercentage)
        if self.vatContent is not None:
            showIndent(outfile, level)
            outfile.write('vatContent=%f,\n' % self.vatContent)
        if self.vatExemption is not None:
            showIndent(outfile, level)
            outfile.write('vatExemption=model_.DetailedReasonType(\n')
            self.vatExemption.exportLiteral(outfile, level, name_='vatExemption')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatOutOfScope is not None:
            showIndent(outfile, level)
            outfile.write('vatOutOfScope=model_.DetailedReasonType(\n')
            self.vatOutOfScope.exportLiteral(outfile, level, name_='vatOutOfScope')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vatDomesticReverseCharge is not None:
            showIndent(outfile, level)
            outfile.write('vatDomesticReverseCharge=%s,\n' % self.vatDomesticReverseCharge)
        if self.marginSchemeIndicator is not None:
            showIndent(outfile, level)
            outfile.write('marginSchemeIndicator=%s,\n' % self.gds_encode(quote_python(self.marginSchemeIndicator)))
        if self.vatAmountMismatch is not None:
            showIndent(outfile, level)
            outfile.write('vatAmountMismatch=model_.VatAmountMismatchType(\n')
            self.vatAmountMismatch.exportLiteral(outfile, level, name_='vatAmountMismatch')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.noVatCharge is not None:
            showIndent(outfile, level)
            outfile.write('noVatCharge=%s,\n' % self.noVatCharge)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'vatPercentage' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatPercentage')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatPercentage')
            self.vatPercentage = fval_
            self.vatPercentage_nsprefix_ = child_.prefix
            # validate type RateType
            self.validate_RateType(self.vatPercentage)
        elif nodeName_ == 'vatContent' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatContent')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatContent')
            self.vatContent = fval_
            self.vatContent_nsprefix_ = child_.prefix
            # validate type RateType
            self.validate_RateType(self.vatContent)
        elif nodeName_ == 'vatExemption':
            obj_ = DetailedReasonType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatExemption = obj_
            obj_.original_tagname_ = 'vatExemption'
        elif nodeName_ == 'vatOutOfScope':
            obj_ = DetailedReasonType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatOutOfScope = obj_
            obj_.original_tagname_ = 'vatOutOfScope'
        elif nodeName_ == 'vatDomesticReverseCharge':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'vatDomesticReverseCharge')
            ival_ = self.gds_validate_boolean(ival_, node, 'vatDomesticReverseCharge')
            self.vatDomesticReverseCharge = ival_
            self.vatDomesticReverseCharge_nsprefix_ = child_.prefix
        elif nodeName_ == 'marginSchemeIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'marginSchemeIndicator')
            value_ = self.gds_validate_string(value_, node, 'marginSchemeIndicator')
            self.marginSchemeIndicator = value_
            self.marginSchemeIndicator_nsprefix_ = child_.prefix
            # validate type MarginSchemeType
            self.validate_MarginSchemeType(self.marginSchemeIndicator)
        elif nodeName_ == 'vatAmountMismatch':
            obj_ = VatAmountMismatchType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.vatAmountMismatch = obj_
            obj_.original_tagname_ = 'vatAmountMismatch'
        elif nodeName_ == 'noVatCharge':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'noVatCharge')
            ival_ = self.gds_validate_boolean(ival_, node, 'noVatCharge')
            self.noVatCharge = ival_
            self.noVatCharge_nsprefix_ = child_.prefix
# end class VatRateType


class VatRateVatDataType(GeneratedsSuper):
    """VatRateVatDataType -- Adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    Á
    FA adatok
    VAT data of given tax rate
    vatRateVatAmount -- Az adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    é
    rt
    é
    kes
    í
    t
    é
    s vagy szolg
    á
    ltat
    á
    sny
    ú
    jt
    á
    s
    Á
    FA
    ö
    sszege a sz
    á
    mla p
    é
    nznem
    é
    ben
    VAT amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    vatRateVatAmountHUF -- Az adott ad
    ó
    m
    é
    rt
    é
    khez tartoz
    ó
    é
    rt
    é
    kes
    í
    t
    é
    s vagy szolg
    á
    ltat
    á
    sny
    ú
    jt
    á
    s
    Á
    FA
    ö
    sszege forintban
    VAT amount of sales or service delivery under a given tax rate expressed in HUF

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, vatRateVatAmount=None, vatRateVatAmountHUF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.vatRateVatAmount = vatRateVatAmount
        self.validate_MonetaryType(self.vatRateVatAmount)
        self.vatRateVatAmount_nsprefix_ = "base"
        self.vatRateVatAmountHUF = vatRateVatAmountHUF
        self.validate_MonetaryType(self.vatRateVatAmountHUF)
        self.vatRateVatAmountHUF_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VatRateVatDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VatRateVatDataType.subclass:
            return VatRateVatDataType.subclass(*args_, **kwargs_)
        else:
            return VatRateVatDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_vatRateVatAmount(self):
        return self.vatRateVatAmount
    def set_vatRateVatAmount(self, vatRateVatAmount):
        self.vatRateVatAmount = vatRateVatAmount
    def get_vatRateVatAmountHUF(self):
        return self.vatRateVatAmountHUF
    def set_vatRateVatAmountHUF(self, vatRateVatAmountHUF):
        self.vatRateVatAmountHUF = vatRateVatAmountHUF
    def validate_MonetaryType(self, value):
        result = True
        # Validate type MonetaryType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on MonetaryType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.vatRateVatAmount is not None or
            self.vatRateVatAmountHUF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateVatDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VatRateVatDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VatRateVatDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VatRateVatDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VatRateVatDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VatRateVatDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='VatRateVatDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vatRateVatAmount is not None:
            namespaceprefix_ = self.vatRateVatAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateVatAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateVatAmount>%s</%svatRateVatAmount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateVatAmount, input_name='vatRateVatAmount'), namespaceprefix_ , eol_))
        if self.vatRateVatAmountHUF is not None:
            namespaceprefix_ = self.vatRateVatAmountHUF_nsprefix_ + ':' if (UseCapturedNS_ and self.vatRateVatAmountHUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svatRateVatAmountHUF>%s</%svatRateVatAmountHUF>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vatRateVatAmountHUF, input_name='vatRateVatAmountHUF'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VatRateVatDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.vatRateVatAmount is not None:
            vatRateVatAmount_ = self.vatRateVatAmount
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateVatAmount').text = self.gds_format_decimal(vatRateVatAmount_)
        if self.vatRateVatAmountHUF is not None:
            vatRateVatAmountHUF_ = self.vatRateVatAmountHUF
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}vatRateVatAmountHUF').text = self.gds_format_decimal(vatRateVatAmountHUF_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VatRateVatDataType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.vatRateVatAmount is not None:
            showIndent(outfile, level)
            outfile.write('vatRateVatAmount=%f,\n' % self.vatRateVatAmount)
        if self.vatRateVatAmountHUF is not None:
            showIndent(outfile, level)
            outfile.write('vatRateVatAmountHUF=%f,\n' % self.vatRateVatAmountHUF)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'vatRateVatAmount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateVatAmount')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateVatAmount')
            self.vatRateVatAmount = fval_
            self.vatRateVatAmount_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateVatAmount)
        elif nodeName_ == 'vatRateVatAmountHUF' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vatRateVatAmountHUF')
            fval_ = self.gds_validate_decimal(fval_, node, 'vatRateVatAmountHUF')
            self.vatRateVatAmountHUF = fval_
            self.vatRateVatAmountHUF_nsprefix_ = child_.prefix
            # validate type MonetaryType
            self.validate_MonetaryType(self.vatRateVatAmountHUF)
# end class VatRateVatDataType


class VehicleType(GeneratedsSuper):
    """VehicleType -- Sz
    á
    razf
    ö
    ldi k
    ö
    zleked
    é
    si eszk
    ö
    z tov
    á
    bbi adatai
    Other data in relation to motorised land vehicle
    engineCapacity -- Henger
    ű
    rtartalom k
    ö
    bcentim
    é
    terben
    Engine capacity in cubic centimetre
    enginePower -- Teljes
    í
    tm
    é
    ny kW-ban
    Engine power in kW
    kms -- Futott kilom
    é
    terek sz
    á
    ma
    Travelled distance in km

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, engineCapacity=None, enginePower=None, kms=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.engineCapacity = engineCapacity
        self.validate_QuantityType(self.engineCapacity)
        self.engineCapacity_nsprefix_ = None
        self.enginePower = enginePower
        self.validate_QuantityType(self.enginePower)
        self.enginePower_nsprefix_ = None
        self.kms = kms
        self.validate_QuantityType(self.kms)
        self.kms_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VehicleType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VehicleType.subclass:
            return VehicleType.subclass(*args_, **kwargs_)
        else:
            return VehicleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_engineCapacity(self):
        return self.engineCapacity
    def set_engineCapacity(self, engineCapacity):
        self.engineCapacity = engineCapacity
    def get_enginePower(self):
        return self.enginePower
    def set_enginePower(self, enginePower):
        self.enginePower = enginePower
    def get_kms(self):
        return self.kms
    def set_kms(self, kms):
        self.kms = kms
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.engineCapacity is not None or
            self.enginePower is not None or
            self.kms is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='VehicleType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VehicleType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VehicleType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VehicleType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VehicleType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VehicleType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='VehicleType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.engineCapacity is not None:
            namespaceprefix_ = self.engineCapacity_nsprefix_ + ':' if (UseCapturedNS_ and self.engineCapacity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sengineCapacity>%s</%sengineCapacity>%s' % (namespaceprefix_ , self.gds_format_decimal(self.engineCapacity, input_name='engineCapacity'), namespaceprefix_ , eol_))
        if self.enginePower is not None:
            namespaceprefix_ = self.enginePower_nsprefix_ + ':' if (UseCapturedNS_ and self.enginePower_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%senginePower>%s</%senginePower>%s' % (namespaceprefix_ , self.gds_format_decimal(self.enginePower, input_name='enginePower'), namespaceprefix_ , eol_))
        if self.kms is not None:
            namespaceprefix_ = self.kms_nsprefix_ + ':' if (UseCapturedNS_ and self.kms_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%skms>%s</%skms>%s' % (namespaceprefix_ , self.gds_format_decimal(self.kms, input_name='kms'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VehicleType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.engineCapacity is not None:
            engineCapacity_ = self.engineCapacity
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}engineCapacity').text = self.gds_format_decimal(engineCapacity_)
        if self.enginePower is not None:
            enginePower_ = self.enginePower
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}enginePower').text = self.gds_format_decimal(enginePower_)
        if self.kms is not None:
            kms_ = self.kms
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}kms').text = self.gds_format_decimal(kms_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VehicleType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.engineCapacity is not None:
            showIndent(outfile, level)
            outfile.write('engineCapacity=%f,\n' % self.engineCapacity)
        if self.enginePower is not None:
            showIndent(outfile, level)
            outfile.write('enginePower=%f,\n' % self.enginePower)
        if self.kms is not None:
            showIndent(outfile, level)
            outfile.write('kms=%f,\n' % self.kms)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'engineCapacity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'engineCapacity')
            fval_ = self.gds_validate_decimal(fval_, node, 'engineCapacity')
            self.engineCapacity = fval_
            self.engineCapacity_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.engineCapacity)
        elif nodeName_ == 'enginePower' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'enginePower')
            fval_ = self.gds_validate_decimal(fval_, node, 'enginePower')
            self.enginePower = fval_
            self.enginePower_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.enginePower)
        elif nodeName_ == 'kms' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'kms')
            fval_ = self.gds_validate_decimal(fval_, node, 'kms')
            self.kms = fval_
            self.kms_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.kms)
# end class VehicleType


class VesselType(GeneratedsSuper):
    """VesselType -- V
    í
    zi j
    á
    rm
    ű
    adatai
    Data of vessel
    length -- Haj
    ó
    hossza m
    é
    terben
    Length of hull in metre
    activityReferred -- É
    rt
    é
    ke true, ha a j
    á
    rm
    ű
    az
    Á
    FA tv. 259.
    §
    25. b) szerinti kiv
    é
    tel al
    á
    tartozik
    The value is true if the means of transport is exempt from VAT as per section 259 [25] (b)
    sailedHours -- Haj
    ó
    zott
    ó
    r
    á
    k sz
    á
    ma
    Number of sailed hours

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, length=None, activityReferred=None, sailedHours=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.length = length
        self.validate_QuantityType(self.length)
        self.length_nsprefix_ = None
        self.activityReferred = activityReferred
        self.activityReferred_nsprefix_ = "xs"
        self.sailedHours = sailedHours
        self.validate_QuantityType(self.sailedHours)
        self.sailedHours_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, VesselType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if VesselType.subclass:
            return VesselType.subclass(*args_, **kwargs_)
        else:
            return VesselType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def get_activityReferred(self):
        return self.activityReferred
    def set_activityReferred(self, activityReferred):
        self.activityReferred = activityReferred
    def get_sailedHours(self):
        return self.sailedHours
    def set_sailedHours(self, sailedHours):
        self.sailedHours = sailedHours
    def validate_QuantityType(self, value):
        result = True
        # Validate type QuantityType, a restriction on common:GenericDecimalType.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.length is not None or
            self.activityReferred is not None or
            self.sailedHours is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='VesselType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('VesselType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'VesselType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='VesselType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='VesselType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='VesselType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:xs="http://www.w3.org/2001/XMLSchema" ', name_='VesselType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.length is not None:
            namespaceprefix_ = self.length_nsprefix_ + ':' if (UseCapturedNS_ and self.length_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slength>%s</%slength>%s' % (namespaceprefix_ , self.gds_format_decimal(self.length, input_name='length'), namespaceprefix_ , eol_))
        if self.activityReferred is not None:
            namespaceprefix_ = self.activityReferred_nsprefix_ + ':' if (UseCapturedNS_ and self.activityReferred_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sactivityReferred>%s</%sactivityReferred>%s' % (namespaceprefix_ , self.gds_format_boolean(self.activityReferred, input_name='activityReferred'), namespaceprefix_ , eol_))
        if self.sailedHours is not None:
            namespaceprefix_ = self.sailedHours_nsprefix_ + ':' if (UseCapturedNS_ and self.sailedHours_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssailedHours>%s</%ssailedHours>%s' % (namespaceprefix_ , self.gds_format_decimal(self.sailedHours, input_name='sailedHours'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='VesselType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/data}' + name_, nsmap=nsmap_)
        if self.length is not None:
            length_ = self.length
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}length').text = self.gds_format_decimal(length_)
        if self.activityReferred is not None:
            activityReferred_ = self.activityReferred
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}activityReferred').text = self.gds_format_boolean(activityReferred_)
        if self.sailedHours is not None:
            sailedHours_ = self.sailedHours
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/data}sailedHours').text = self.gds_format_decimal(sailedHours_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='VesselType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.length is not None:
            showIndent(outfile, level)
            outfile.write('length=%f,\n' % self.length)
        if self.activityReferred is not None:
            showIndent(outfile, level)
            outfile.write('activityReferred=%s,\n' % self.activityReferred)
        if self.sailedHours is not None:
            showIndent(outfile, level)
            outfile.write('sailedHours=%f,\n' % self.sailedHours)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'length' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'length')
            fval_ = self.gds_validate_decimal(fval_, node, 'length')
            self.length = fval_
            self.length_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.length)
        elif nodeName_ == 'activityReferred':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'activityReferred')
            ival_ = self.gds_validate_boolean(ival_, node, 'activityReferred')
            self.activityReferred = ival_
            self.activityReferred_nsprefix_ = child_.prefix
        elif nodeName_ == 'sailedHours' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'sailedHours')
            fval_ = self.gds_validate_decimal(fval_, node, 'sailedHours')
            self.sailedHours = fval_
            self.sailedHours_nsprefix_ = child_.prefix
            # validate type QuantityType
            self.validate_QuantityType(self.sailedHours)
# end class VesselType


class InvoiceData(InvoiceDataType):
    """InvoiceData -- XML root element, sz
    á
    mla vagy m
    ó
    dos
    í
    t
    á
    s adatait le
    í
    r
    ó
    t
    í
    pus, amelyet BASE64 k
    ó
    doltan tartalmaz az invoiceApi s
    é
    male
    í
    r
    ó
    invoiceData elementje
    XML root element, invoice or modification data type in BASE64 encoding, equivalent with the invoiceApi schema definition's invoiceData element

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = InvoiceDataType
    def __init__(self, invoiceNumber=None, invoiceIssueDate=None, completenessIndicator=None, invoiceMain=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("InvoiceData"), self).__init__(invoiceNumber, invoiceIssueDate, completenessIndicator, invoiceMain,  **kwargs_)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceData.subclass:
            return InvoiceData.subclass(*args_, **kwargs_)
        else:
            return InvoiceData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (
            super(InvoiceData, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"', name_='InvoiceData', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceData')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceData':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceData')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceData', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceData'):
        super(InvoiceData, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceData')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"', name_='InvoiceData', fromsubclass_=False, pretty_print=True):
        super(InvoiceData, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='InvoiceData', mapping_=None, nsmap_=None):
        element = super(InvoiceData, self).to_etree(parent_element, name_, mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='InvoiceData'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(InvoiceData, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(InvoiceData, self)._exportLiteralChildren(outfile, level, name_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(InvoiceData, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(InvoiceData, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class InvoiceData


class MetricDefinitionType(GeneratedsSuper):
    """MetricDefinitionType -- Metrika defin
    í
    ci
    ó
    t
    í
    pus
    Metric definition type
    metricName -- Metrika neve
    Metric's name
    metricType -- Metrika t
    í
    pusa
    Metric's type
    metricDescription -- Metrika le
    í
    r
    á
    sa
    Metric's description

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, metricName=None, metricType=None, metricDescription=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.metricName = metricName
        self.validate_SimpleText200NotBlankType(self.metricName)
        self.metricName_nsprefix_ = "common"
        self.metricType = metricType
        self.validate_MetricTypeType(self.metricType)
        self.metricType_nsprefix_ = None
        if metricDescription is None:
            self.metricDescription = []
        else:
            self.metricDescription = metricDescription
        self.metricDescription_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetricDefinitionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetricDefinitionType.subclass:
            return MetricDefinitionType.subclass(*args_, **kwargs_)
        else:
            return MetricDefinitionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_metricName(self):
        return self.metricName
    def set_metricName(self, metricName):
        self.metricName = metricName
    def get_metricType(self):
        return self.metricType
    def set_metricType(self, metricType):
        self.metricType = metricType
    def get_metricDescription(self):
        return self.metricDescription
    def set_metricDescription(self, metricDescription):
        self.metricDescription = metricDescription
    def add_metricDescription(self, value):
        self.metricDescription.append(value)
    def insert_metricDescription_at(self, index, value):
        self.metricDescription.insert(index, value)
    def replace_metricDescription_at(self, index, value):
        self.metricDescription[index] = value
    def validate_SimpleText200NotBlankType(self, value):
        result = True
        # Validate type SimpleText200NotBlankType, a restriction on AtomicStringType200.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 200:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText200NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText200NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText200NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText200NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText200NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def validate_MetricTypeType(self, value):
        result = True
        # Validate type MetricTypeType, a restriction on common:AtomicStringType15.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['COUNTER', 'GAUGE', 'HISTOGRAM', 'SUMMARY']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on MetricTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on MetricTypeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on MetricTypeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.metricName is not None or
            self.metricType is not None or
            self.metricDescription
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='MetricDefinitionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetricDefinitionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetricDefinitionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetricDefinitionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetricDefinitionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetricDefinitionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='MetricDefinitionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.metricName is not None:
            namespaceprefix_ = self.metricName_nsprefix_ + ':' if (UseCapturedNS_ and self.metricName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smetricName>%s</%smetricName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.metricName), input_name='metricName')), namespaceprefix_ , eol_))
        if self.metricType is not None:
            namespaceprefix_ = self.metricType_nsprefix_ + ':' if (UseCapturedNS_ and self.metricType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smetricType>%s</%smetricType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.metricType), input_name='metricType')), namespaceprefix_ , eol_))
        for metricDescription_ in self.metricDescription:
            namespaceprefix_ = self.metricDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.metricDescription_nsprefix_) else ''
            metricDescription_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metricDescription', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MetricDefinitionType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.metricName is not None:
            metricName_ = self.metricName
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}metricName').text = self.gds_format_string(metricName_)
        if self.metricType is not None:
            metricType_ = self.metricType
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}metricType').text = self.gds_format_string(metricType_)
        for metricDescription_ in self.metricDescription:
            metricDescription_.to_etree(element, name_='metricDescription', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MetricDefinitionType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.metricName is not None:
            showIndent(outfile, level)
            outfile.write('metricName=%s,\n' % self.gds_encode(quote_python(self.metricName)))
        if self.metricType is not None:
            showIndent(outfile, level)
            outfile.write('metricType=%s,\n' % self.gds_encode(quote_python(self.metricType)))
        showIndent(outfile, level)
        outfile.write('metricDescription=[\n')
        level += 1
        for metricDescription_ in self.metricDescription:
            showIndent(outfile, level)
            outfile.write('model_.MetricDescriptionType(\n')
            metricDescription_.exportLiteral(outfile, level, name_='MetricDescriptionType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'metricName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'metricName')
            value_ = self.gds_validate_string(value_, node, 'metricName')
            self.metricName = value_
            self.metricName_nsprefix_ = child_.prefix
            # validate type SimpleText200NotBlankType
            self.validate_SimpleText200NotBlankType(self.metricName)
        elif nodeName_ == 'metricType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'metricType')
            value_ = self.gds_validate_string(value_, node, 'metricType')
            self.metricType = value_
            self.metricType_nsprefix_ = child_.prefix
            # validate type MetricTypeType
            self.validate_MetricTypeType(self.metricType)
        elif nodeName_ == 'metricDescription':
            obj_ = MetricDescriptionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metricDescription.append(obj_)
            obj_.original_tagname_ = 'metricDescription'
# end class MetricDefinitionType


class MetricDescriptionType(GeneratedsSuper):
    """MetricDescriptionType -- Metrika le
    í
    r
    á
    s t
    í
    pus
    Metric description type
    language -- Nyelv megnevez
    é
    s
    Language naming
    localizedDescription -- Lokaliz
    á
    lt le
    í
    r
    á
    s
    Localized description

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, language=None, localizedDescription=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.language = language
        self.validate_LanguageType(self.language)
        self.language_nsprefix_ = None
        self.localizedDescription = localizedDescription
        self.validate_SimpleText512NotBlankType(self.localizedDescription)
        self.localizedDescription_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetricDescriptionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetricDescriptionType.subclass:
            return MetricDescriptionType.subclass(*args_, **kwargs_)
        else:
            return MetricDescriptionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_language(self):
        return self.language
    def set_language(self, language):
        self.language = language
    def get_localizedDescription(self):
        return self.localizedDescription
    def set_localizedDescription(self, localizedDescription):
        self.localizedDescription = localizedDescription
    def validate_LanguageType(self, value):
        result = True
        # Validate type LanguageType, a restriction on common:AtomicStringType2.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            value = value
            enumerations = ['HU', 'EN', 'DE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LanguageType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LanguageType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LanguageType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_SimpleText512NotBlankType(self, value):
        result = True
        # Validate type SimpleText512NotBlankType, a restriction on AtomicStringType512.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 512:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SimpleText512NotBlankType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SimpleText512NotBlankType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SimpleText512NotBlankType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SimpleText512NotBlankType_patterns_, ))
                result = False
        return result
    validate_SimpleText512NotBlankType_patterns_ = [['^(.*[^\\s].*)$']]
    def _hasContent(self):
        if (
            self.language is not None or
            self.localizedDescription is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='MetricDescriptionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetricDescriptionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetricDescriptionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetricDescriptionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetricDescriptionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetricDescriptionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics"  xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" ', name_='MetricDescriptionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.language is not None:
            namespaceprefix_ = self.language_nsprefix_ + ':' if (UseCapturedNS_ and self.language_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slanguage>%s</%slanguage>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.language), input_name='language')), namespaceprefix_ , eol_))
        if self.localizedDescription is not None:
            namespaceprefix_ = self.localizedDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.localizedDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slocalizedDescription>%s</%slocalizedDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.localizedDescription), input_name='localizedDescription')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='MetricDescriptionType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.language is not None:
            language_ = self.language
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}language').text = self.gds_format_string(language_)
        if self.localizedDescription is not None:
            localizedDescription_ = self.localizedDescription
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}localizedDescription').text = self.gds_format_string(localizedDescription_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MetricDescriptionType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.language is not None:
            showIndent(outfile, level)
            outfile.write('language=%s,\n' % self.gds_encode(quote_python(self.language)))
        if self.localizedDescription is not None:
            showIndent(outfile, level)
            outfile.write('localizedDescription=%s,\n' % self.gds_encode(quote_python(self.localizedDescription)))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'language':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'language')
            value_ = self.gds_validate_string(value_, node, 'language')
            self.language = value_
            self.language_nsprefix_ = child_.prefix
            # validate type LanguageType
            self.validate_LanguageType(self.language)
        elif nodeName_ == 'localizedDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'localizedDescription')
            value_ = self.gds_validate_string(value_, node, 'localizedDescription')
            self.localizedDescription = value_
            self.localizedDescription_nsprefix_ = child_.prefix
            # validate type SimpleText512NotBlankType
            self.validate_SimpleText512NotBlankType(self.localizedDescription)
# end class MetricDescriptionType


class MetricType(GeneratedsSuper):
    """MetricType -- Metrika t
    í
    pus
    Metric data type
    metricDefinition -- Metrika defin
    í
    ci
    ó
    Metric definition
    metricValues -- Metrika
    é
    rt
    é
    kek
    Metric values

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, metricDefinition=None, metricValues=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.metricDefinition = metricDefinition
        self.metricDefinition_nsprefix_ = None
        if metricValues is None:
            self.metricValues = []
        else:
            self.metricValues = metricValues
        self.metricValues_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetricType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetricType.subclass:
            return MetricType.subclass(*args_, **kwargs_)
        else:
            return MetricType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_metricDefinition(self):
        return self.metricDefinition
    def set_metricDefinition(self, metricDefinition):
        self.metricDefinition = metricDefinition
    def get_metricValues(self):
        return self.metricValues
    def set_metricValues(self, metricValues):
        self.metricValues = metricValues
    def add_metricValues(self, value):
        self.metricValues.append(value)
    def insert_metricValues_at(self, index, value):
        self.metricValues.insert(index, value)
    def replace_metricValues_at(self, index, value):
        self.metricValues[index] = value
    def _hasContent(self):
        if (
            self.metricDefinition is not None or
            self.metricValues
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='MetricType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetricType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetricType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetricType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetricType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetricType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='MetricType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.metricDefinition is not None:
            namespaceprefix_ = self.metricDefinition_nsprefix_ + ':' if (UseCapturedNS_ and self.metricDefinition_nsprefix_) else ''
            self.metricDefinition.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metricDefinition', pretty_print=pretty_print)
        for metricValues_ in self.metricValues:
            namespaceprefix_ = self.metricValues_nsprefix_ + ':' if (UseCapturedNS_ and self.metricValues_nsprefix_) else ''
            metricValues_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metricValues', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MetricType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.metricDefinition is not None:
            metricDefinition_ = self.metricDefinition
            metricDefinition_.to_etree(element, name_='metricDefinition', mapping_=mapping_, nsmap_=nsmap_)
        for metricValues_ in self.metricValues:
            metricValues_.to_etree(element, name_='metricValues', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MetricType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.metricDefinition is not None:
            showIndent(outfile, level)
            outfile.write('metricDefinition=model_.MetricDefinitionType(\n')
            self.metricDefinition.exportLiteral(outfile, level, name_='metricDefinition')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('metricValues=[\n')
        level += 1
        for metricValues_ in self.metricValues:
            showIndent(outfile, level)
            outfile.write('model_.MetricValueType(\n')
            metricValues_.exportLiteral(outfile, level, name_='MetricValueType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'metricDefinition':
            obj_ = MetricDefinitionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metricDefinition = obj_
            obj_.original_tagname_ = 'metricDefinition'
        elif nodeName_ == 'metricValues':
            obj_ = MetricValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metricValues.append(obj_)
            obj_.original_tagname_ = 'metricValues'
# end class MetricType


class MetricValueType(GeneratedsSuper):
    """MetricValueType -- Metrika
    é
    rt
    é
    k t
    í
    pus
    Metric value type
    value -- Metrika
    é
    rt
    é
    ke
    Metric's value
    timestamp -- Metrika
    é
    rt
    é
    k
    é
    nek id
    ő
    pontja UTC id
    ő
    ben
    Time of metric value in UTC time

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, value=None, timestamp=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.validate_GenericDecimalType(self.value)
        self.value_nsprefix_ = "common"
        if isinstance(timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = timestamp
        self.timestamp = initvalue_
        self.timestamp_nsprefix_ = "base"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetricValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetricValueType.subclass:
            return MetricValueType.subclass(*args_, **kwargs_)
        else:
            return MetricValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_timestamp(self):
        return self.timestamp
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
    def validate_GenericDecimalType(self, value):
        result = True
        # Validate type GenericDecimalType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime.datetime.fromisostring('2010-01-01T00:00:00.000000').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceTimestampType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceTimestampType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceTimestampType_patterns_, ))
                result = False
        return result
    validate_InvoiceTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z)$']]
    def _hasContent(self):
        if (
            self.value is not None or
            self.timestamp is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='MetricValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetricValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetricValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetricValueType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetricValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetricValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base" ', name_='MetricValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespaceprefix_ , self.gds_format_decimal(self.value, input_name='value'), namespaceprefix_ , eol_))
        if self.timestamp is not None:
            namespaceprefix_ = self.timestamp_nsprefix_ + ':' if (UseCapturedNS_ and self.timestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stimestamp>%s</%stimestamp>%s' % (namespaceprefix_ , self.gds_format_datetime(self.timestamp, input_name='timestamp'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='MetricValueType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}value').text = self.gds_format_decimal(value_)
        if self.timestamp is not None:
            timestamp_ = self.timestamp
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}timestamp').text = self.gds_format_datetime(timestamp_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MetricValueType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.value is not None:
            showIndent(outfile, level)
            outfile.write('value=%f,\n' % self.value)
        if self.timestamp is not None:
            showIndent(outfile, level)
            outfile.write('timestamp=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'value')
            fval_ = self.gds_validate_decimal(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
            # validate type GenericDecimalType
            self.validate_GenericDecimalType(self.value)
        elif nodeName_ == 'timestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.timestamp = dval_
            self.timestamp_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.timestamp)
# end class MetricValueType


class QueryServiceMetricsListResponseType(GeneratedsSuper):
    """QueryServiceMetricsListResponseType -- A GET /queryServiceMetrics/list REST oper
    á
    ci
    ó
    v
    á
    lasz t
    í
    pusa
    Response type of the GET /queryServiceMetrics/list REST operation
    metricDefinition -- Metrika defin
    í
    ci
    ó
    i
    Metric definitions

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, metricDefinition=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if metricDefinition is None:
            self.metricDefinition = []
        else:
            self.metricDefinition = metricDefinition
        self.metricDefinition_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryServiceMetricsListResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryServiceMetricsListResponseType.subclass:
            return QueryServiceMetricsListResponseType.subclass(*args_, **kwargs_)
        else:
            return QueryServiceMetricsListResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_metricDefinition(self):
        return self.metricDefinition
    def set_metricDefinition(self, metricDefinition):
        self.metricDefinition = metricDefinition
    def add_metricDefinition(self, value):
        self.metricDefinition.append(value)
    def insert_metricDefinition_at(self, index, value):
        self.metricDefinition.insert(index, value)
    def replace_metricDefinition_at(self, index, value):
        self.metricDefinition[index] = value
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.metricDefinition
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryServiceMetricsListResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryServiceMetricsListResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryServiceMetricsListResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryServiceMetricsListResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryServiceMetricsListResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryServiceMetricsListResponseType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryServiceMetricsListResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for metricDefinition_ in self.metricDefinition:
            namespaceprefix_ = self.metricDefinition_nsprefix_ + ':' if (UseCapturedNS_ and self.metricDefinition_nsprefix_) else ''
            metricDefinition_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metricDefinition', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryServiceMetricsListResponseType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        for metricDefinition_ in self.metricDefinition:
            metricDefinition_.to_etree(element, name_='metricDefinition', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryServiceMetricsListResponseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('metricDefinition=[\n')
        level += 1
        for metricDefinition_ in self.metricDefinition:
            showIndent(outfile, level)
            outfile.write('model_.MetricDefinitionType(\n')
            metricDefinition_.exportLiteral(outfile, level, name_='MetricDefinitionType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'metricDefinition':
            obj_ = MetricDefinitionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metricDefinition.append(obj_)
            obj_.original_tagname_ = 'metricDefinition'
# end class QueryServiceMetricsListResponseType


class QueryServiceMetricsResponseType(GeneratedsSuper):
    """QueryServiceMetricsResponseType -- A GET /queryServiceMetrics REST oper
    á
    ci
    ó
    v
    á
    lasz t
    í
    pusa
    Response type of the GET /queryServiceMetrics REST operation
    result -- Alap v
    á
    laszeredm
    é
    ny adatok
    Basic result data
    metricsLastUpdateTime -- A metrik
    á
    k utols
    ó
    friss
    í
    t
    é
    s
    é
    nek id
    ő
    pontja UTC id
    ő
    ben
    Last update time of metrics in UTC time
    metric -- Metrika adatai
    Metric data

    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, result=None, metricsLastUpdateTime=None, metric=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.result = result
        self.result_nsprefix_ = "common"
        if isinstance(metricsLastUpdateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(metricsLastUpdateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = metricsLastUpdateTime
        self.metricsLastUpdateTime = initvalue_
        self.metricsLastUpdateTime_nsprefix_ = "base"
        if metric is None:
            self.metric = []
        else:
            self.metric = metric
        self.metric_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryServiceMetricsResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryServiceMetricsResponseType.subclass:
            return QueryServiceMetricsResponseType.subclass(*args_, **kwargs_)
        else:
            return QueryServiceMetricsResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_result(self):
        return self.result
    def set_result(self, result):
        self.result = result
    def get_metricsLastUpdateTime(self):
        return self.metricsLastUpdateTime
    def set_metricsLastUpdateTime(self, metricsLastUpdateTime):
        self.metricsLastUpdateTime = metricsLastUpdateTime
    def get_metric(self):
        return self.metric
    def set_metric(self, metric):
        self.metric = metric
    def add_metric(self, value):
        self.metric.append(value)
    def insert_metric_at(self, index, value):
        self.metric.insert(index, value)
    def replace_metric_at(self, index, value):
        self.metric[index] = value
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_InvoiceTimestampType(self, value):
        result = True
        # Validate type InvoiceTimestampType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if value < datetime.datetime.fromisostring('2010-01-01T00:00:00.000000').replace(tzinfo=pytz.UTC):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on InvoiceTimestampType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_InvoiceTimestampType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_InvoiceTimestampType_patterns_, ))
                result = False
        return result
    validate_InvoiceTimestampType_patterns_ = [['^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(.\\d{1,3})?Z)$']]
    def _hasContent(self):
        if (
            self.result is not None or
            self.metricsLastUpdateTime is not None or
            self.metric
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryServiceMetricsResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryServiceMetricsResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryServiceMetricsResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryServiceMetricsResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryServiceMetricsResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryServiceMetricsResponseType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"  xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base"  xmlns:None="http://schemas.nav.gov.hu/OSA/3.0/metrics" ', name_='QueryServiceMetricsResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.result is not None:
            namespaceprefix_ = self.result_nsprefix_ + ':' if (UseCapturedNS_ and self.result_nsprefix_) else ''
            self.result.export(outfile, level, namespaceprefix_, namespacedef_='', name_='result', pretty_print=pretty_print)
        if self.metricsLastUpdateTime is not None:
            namespaceprefix_ = self.metricsLastUpdateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.metricsLastUpdateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smetricsLastUpdateTime>%s</%smetricsLastUpdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.metricsLastUpdateTime, input_name='metricsLastUpdateTime'), namespaceprefix_ , eol_))
        for metric_ in self.metric:
            namespaceprefix_ = self.metric_nsprefix_ + ':' if (UseCapturedNS_ and self.metric_nsprefix_) else ''
            metric_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metric', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryServiceMetricsResponseType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}' + name_, nsmap=nsmap_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.result is not None:
            result_ = self.result
            result_.to_etree(element, name_='result', mapping_=mapping_, nsmap_=nsmap_)
        if self.metricsLastUpdateTime is not None:
            metricsLastUpdateTime_ = self.metricsLastUpdateTime
            etree_.SubElement(element, '{http://schemas.nav.gov.hu/OSA/3.0/metrics}metricsLastUpdateTime').text = self.gds_format_datetime(metricsLastUpdateTime_)
        for metric_ in self.metric:
            metric_.to_etree(element, name_='metric', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryServiceMetricsResponseType'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def _exportLiteralChildren(self, outfile, level, name_):
        if self.result is not None:
            showIndent(outfile, level)
            outfile.write('result=model_.BasicResultType(\n')
            self.result.exportLiteral(outfile, level, name_='result')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.metricsLastUpdateTime is not None:
            showIndent(outfile, level)
            outfile.write('metricsLastUpdateTime=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.metricsLastUpdateTime, input_name='metricsLastUpdateTime'))
        showIndent(outfile, level)
        outfile.write('metric=[\n')
        level += 1
        for metric_ in self.metric:
            showIndent(outfile, level)
            outfile.write('model_.MetricType(\n')
            metric_.exportLiteral(outfile, level, name_='MetricType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'result':
            class_obj_ = self.get_class_obj_(child_, BasicResultType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.result = obj_
            obj_.original_tagname_ = 'result'
        elif nodeName_ == 'metricsLastUpdateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.metricsLastUpdateTime = dval_
            self.metricsLastUpdateTime_nsprefix_ = child_.prefix
            # validate type InvoiceTimestampType
            self.validate_InvoiceTimestampType(self.metricsLastUpdateTime)
        elif nodeName_ == 'metric':
            obj_ = MetricType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metric.append(obj_)
            obj_.original_tagname_ = 'metric'
# end class QueryServiceMetricsResponseType


class QueryServiceMetricsListResponse(QueryServiceMetricsListResponseType):
    """QueryServiceMetricsListResponse -- A GET /queryServiceMetrics/list REST oper
    á
    ci
    ó
    v
    á
    lasz
    á
    nak root elementje
    Response root element of the GET /queryServiceMetrics/list REST operation
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = QueryServiceMetricsListResponseType
    def __init__(self, metricDefinition=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("QueryServiceMetricsListResponse"), self).__init__(metricDefinition,  **kwargs_)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryServiceMetricsListResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryServiceMetricsListResponse.subclass:
            return QueryServiceMetricsListResponse.subclass(*args_, **kwargs_)
        else:
            return QueryServiceMetricsListResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (
            super(QueryServiceMetricsListResponse, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"', name_='QueryServiceMetricsListResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryServiceMetricsListResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryServiceMetricsListResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryServiceMetricsListResponse')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryServiceMetricsListResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryServiceMetricsListResponse'):
        super(QueryServiceMetricsListResponse, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryServiceMetricsListResponse')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"', name_='QueryServiceMetricsListResponse', fromsubclass_=False, pretty_print=True):
        super(QueryServiceMetricsListResponse, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryServiceMetricsListResponse', mapping_=None, nsmap_=None):
        element = super(QueryServiceMetricsListResponse, self).to_etree(parent_element, name_, mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryServiceMetricsListResponse'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(QueryServiceMetricsListResponse, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(QueryServiceMetricsListResponse, self)._exportLiteralChildren(outfile, level, name_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(QueryServiceMetricsListResponse, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(QueryServiceMetricsListResponse, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class QueryServiceMetricsListResponse


class QueryServiceMetricsResponse(QueryServiceMetricsResponseType):
    """QueryServiceMetricsResponse -- A GET /queryServiceMetrics REST oper
    á
    ci
    ó
    v
    á
    lasz
    á
    nak root elementje
    Response root element of the GET /queryServiceMetrics REST operation
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = QueryServiceMetricsResponseType
    def __init__(self, result=None, metricsLastUpdateTime=None, metric=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("QueryServiceMetricsResponse"), self).__init__(result, metricsLastUpdateTime, metric,  **kwargs_)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryServiceMetricsResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryServiceMetricsResponse.subclass:
            return QueryServiceMetricsResponse.subclass(*args_, **kwargs_)
        else:
            return QueryServiceMetricsResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (
            super(QueryServiceMetricsResponse, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"', name_='QueryServiceMetricsResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryServiceMetricsResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'QueryServiceMetricsResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryServiceMetricsResponse')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryServiceMetricsResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryServiceMetricsResponse'):
        super(QueryServiceMetricsResponse, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryServiceMetricsResponse')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://schemas.nav.gov.hu/NTCA/1.0/common"', name_='QueryServiceMetricsResponse', fromsubclass_=False, pretty_print=True):
        super(QueryServiceMetricsResponse, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='QueryServiceMetricsResponse', mapping_=None, nsmap_=None):
        element = super(QueryServiceMetricsResponse, self).to_etree(parent_element, name_, mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryServiceMetricsResponse'):
        level += 1
        already_processed = set()
        self._exportLiteralAttributes(outfile, level, already_processed, name_)
        if self._hasContent():
            self._exportLiteralChildren(outfile, level, name_)
    def _exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(QueryServiceMetricsResponse, self)._exportLiteralAttributes(outfile, level, already_processed, name_)
    def _exportLiteralChildren(self, outfile, level, name_):
        super(QueryServiceMetricsResponse, self)._exportLiteralChildren(outfile, level, name_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(QueryServiceMetricsResponse, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(QueryServiceMetricsResponse, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class QueryServiceMetricsResponse


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'BasicHeaderType'
        rootClass = BasicHeaderType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'BasicHeaderType'
        rootClass = BasicHeaderType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'BasicHeaderType'
        rootClass = BasicHeaderType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:ns2="http://schemas.nav.gov.hu/NTCA/1.0/common"')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'BasicHeaderType'
        rootClass = BasicHeaderType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from online_invoice import *\n\n')
        sys.stdout.write('import online_invoice as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://schemas.nav.gov.hu/NTCA/1.0/common': [('AtomicStringType100',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType1024',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType128',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType15',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType16',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType2',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType200',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType2048',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType255',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType256',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType32',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType4',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType4000',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType50',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType512',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType64',
                                                'common.xsd',
                                                'ST'),
                                               ('AtomicStringType8',
                                                'common.xsd',
                                                'ST'),
                                               ('GenericDateType',
                                                'common.xsd',
                                                'ST'),
                                               ('GenericDecimalType',
                                                'common.xsd',
                                                'ST'),
                                               ('GenericTimestampType',
                                                'common.xsd',
                                                'ST'),
                                               ('SHA256Type',
                                                'common.xsd',
                                                'ST'),
                                               ('SHA512Type',
                                                'common.xsd',
                                                'ST'),
                                               ('SimpleText100NotBlankType',
                                                'common.xsd',
                                                'ST'),
                                               ('SimpleText1024NotBlankType',
                                                'common.xsd',
                                                'ST'),
                                               ('SimpleText15NotBlankType',
                                                'common.xsd',
                                                'ST'),
                                               ('SimpleText200NotBlankType',
                                                'common.xsd',
                                                'ST'),
                                               ('SimpleText255NotBlankType',
                                                'common.xsd',
                                                'ST'),
                                               ('SimpleText50NotBlankType',
                                                'common.xsd',
                                                'ST'),
                                               ('SimpleText512NotBlankType',
                                                'common.xsd',
                                                'ST'),
                                               ('BankAccountNumberType',
                                                'common.xsd',
                                                'ST'),
                                               ('CommunityVatNumberType',
                                                'common.xsd',
                                                'ST'),
                                               ('CountryCodeType',
                                                'common.xsd',
                                                'ST'),
                                               ('CountyCodeType',
                                                'common.xsd',
                                                'ST'),
                                               ('CurrencyType',
                                                'common.xsd',
                                                'ST'),
                                               ('PlateNumberType',
                                                'common.xsd',
                                                'ST'),
                                               ('PostalCodeType',
                                                'common.xsd',
                                                'ST'),
                                               ('TaxpayerIdType',
                                                'common.xsd',
                                                'ST'),
                                               ('VatCodeType',
                                                'common.xsd',
                                                'ST'),
                                               ('BusinessResultCodeType',
                                                'common.xsd',
                                                'ST'),
                                               ('EntityIdType',
                                                'common.xsd',
                                                'ST'),
                                               ('FunctionCodeType',
                                                'common.xsd',
                                                'ST'),
                                               ('LoginType',
                                                'common.xsd',
                                                'ST'),
                                               ('RequestPageType',
                                                'common.xsd',
                                                'ST'),
                                               ('ResponsePageType',
                                                'common.xsd',
                                                'ST'),
                                               ('TechnicalResultCodeType',
                                                'common.xsd',
                                                'ST'),
                                               ('BasicHeaderType',
                                                'common.xsd',
                                                'CT'),
                                               ('BasicRequestType',
                                                'common.xsd',
                                                'CT'),
                                               ('BasicResponseType',
                                                'common.xsd',
                                                'CT'),
                                               ('BasicResultType',
                                                'common.xsd',
                                                'CT'),
                                               ('CryptoType',
                                                'common.xsd',
                                                'CT'),
                                               ('GeneralErrorHeaderResponseType',
                                                'common.xsd',
                                                'CT'),
                                               ('NotificationsType',
                                                'common.xsd',
                                                'CT'),
                                               ('NotificationType',
                                                'common.xsd',
                                                'CT'),
                                               ('TechnicalValidationResultType',
                                                'common.xsd',
                                                'CT'),
                                               ('UserHeaderType',
                                                'common.xsd',
                                                'CT')],
 'http://schemas.nav.gov.hu/OSA/3.0/annul': [('AnnulmentCodeType',
                                              'invoiceAnnulment.xsd',
                                              'ST'),
                                             ('InvoiceAnnulmentType',
                                              'invoiceAnnulment.xsd',
                                              'CT')],
 'http://schemas.nav.gov.hu/OSA/3.0/api': [('AnnulmentVerificationStatusType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('IncorporationType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('InvoiceDirectionType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('InvoiceStatusType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('ManageAnnulmentOperationType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('ManageInvoiceOperationType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('OriginalRequestVersionType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('QueryNameType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('QueryOperatorType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('RequestStatusType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('SoftwareIdType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('SoftwareOperationType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('SourceType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('TaxpayerAddressTypeType',
                                            'invoiceApi.xsd',
                                            'ST'),
                                           ('AdditionalQueryParamsType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('AnnulmentDataType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('AnnulmentOperationListType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('AnnulmentOperationType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('AuditDataType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('BasicOnlineInvoiceRequestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('BasicOnlineInvoiceResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('BusinessValidationResultType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('DateIntervalParamType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('DateTimeIntervalParamType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('GeneralErrorResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceChainDigestResultType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceChainDigestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceChainElementType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceChainQueryType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceDataResultType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceDigestResultType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceDigestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceLinesType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceNumberQueryType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceOperationListType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceOperationType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceQueryParamsType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('InvoiceReferenceDataType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('ManageAnnulmentRequestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('ManageInvoiceRequestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('MandatoryQueryParamsType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('NewCreatedLinesType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('PointerType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('ProcessingResultListType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('ProcessingResultType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryInvoiceChainDigestRequestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryInvoiceChainDigestResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryInvoiceCheckResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryInvoiceDataRequestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryInvoiceDataResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryInvoiceDigestRequestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryInvoiceDigestResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryTaxpayerRequestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryTaxpayerResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryTransactionListRequestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryTransactionListResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryTransactionStatusRequestType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('QueryTransactionStatusResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('RelationalQueryParamsType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('RelationQueryDateType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('RelationQueryMonetaryType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('SoftwareType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('TaxpayerAddressItemType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('TaxpayerAddressListType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('TaxpayerDataType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('TokenExchangeResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('TransactionListResultType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('TransactionQueryParamsType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('TransactionResponseType',
                                            'invoiceApi.xsd',
                                            'CT'),
                                           ('TransactionType',
                                            'invoiceApi.xsd',
                                            'CT')],
 'http://schemas.nav.gov.hu/OSA/3.0/base': [('InvoiceAppearanceType',
                                             'invoiceBase.xsd',
                                             'ST'),
                                            ('InvoiceCategoryType',
                                             'invoiceBase.xsd',
                                             'ST'),
                                            ('InvoiceDateType',
                                             'invoiceBase.xsd',
                                             'ST'),
                                            ('InvoiceIndexType',
                                             'invoiceBase.xsd',
                                             'ST'),
                                            ('InvoiceTimestampType',
                                             'invoiceBase.xsd',
                                             'ST'),
                                            ('InvoiceUnboundedIndexType',
                                             'invoiceBase.xsd',
                                             'ST'),
                                            ('LineNumberType',
                                             'invoiceBase.xsd',
                                             'ST'),
                                            ('MonetaryType',
                                             'invoiceBase.xsd',
                                             'ST'),
                                            ('PaymentMethodType',
                                             'invoiceBase.xsd',
                                             'ST'),
                                            ('AddressType',
                                             'invoiceBase.xsd',
                                             'CT'),
                                            ('DetailedAddressType',
                                             'invoiceBase.xsd',
                                             'CT'),
                                            ('SimpleAddressType',
                                             'invoiceBase.xsd',
                                             'CT'),
                                            ('TaxNumberType',
                                             'invoiceBase.xsd',
                                             'CT')],
 'http://schemas.nav.gov.hu/OSA/3.0/data': [('CustomerVatStatusType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('DataNameType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('EkaerIdType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('ExchangeRateType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('LineNatureIndicatorType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('LineOperationType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('MarginSchemeType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('ProductCodeCategoryType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('ProductCodeValueType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('ProductFeeMeasuringUnitType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('ProductFeeOperationType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('ProductStreamType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('QuantityType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('RateType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('TakeoverType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('UnitOfMeasureType',
                                             'invoiceData.xsd',
                                             'ST'),
                                            ('AdditionalDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('AdvanceDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('AdvancePaymentDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('AggregateInvoiceLineDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('AircraftType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('BatchInvoiceType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ContractNumbersType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ConventionalInvoiceInfoType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('CostCentersType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('CustomerCompanyCodesType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('CustomerDeclarationType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('CustomerInfoType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('CustomerTaxNumberType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('CustomerVatDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('DealerCodesType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('DeliveryNotesType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('DetailedReasonType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('DieselOilPurchaseType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('DiscountDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('EkaerIdsType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('FiscalRepresentativeType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('GeneralLedgerAccountNumbersType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('GlnNumbersType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('InvoiceDetailType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('InvoiceDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('InvoiceHeadType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('InvoiceMainType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('InvoiceReferenceType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('InvoiceType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ItemNumbersType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('LineAmountsNormalType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('LineAmountsSimplifiedType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('LineGrossAmountDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('LineModificationReferenceType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('LineNetAmountDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('LinesType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('LineType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('LineVatDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('MaterialNumbersType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('NewTransportMeanType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('OrderNumbersType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('PaymentEvidenceDocumentDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ProductCodesType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ProductCodeType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ProductFeeClauseType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ProductFeeDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ProductFeeSummaryType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ProductFeeTakeoverDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ProjectNumbersType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ReferencesToOtherLinesType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('ShippingDatesType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('SummaryByVatRateType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('SummaryGrossDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('SummaryNormalType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('SummarySimplifiedType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('SummaryType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('SupplierCompanyCodesType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('SupplierInfoType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('VatAmountMismatchType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('VatRateGrossDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('VatRateNetDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('VatRateType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('VatRateVatDataType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('VehicleType',
                                             'invoiceData.xsd',
                                             'CT'),
                                            ('VesselType',
                                             'invoiceData.xsd',
                                             'CT')],
 'http://schemas.nav.gov.hu/OSA/3.0/metrics': [('LanguageType',
                                                'serviceMetrics.xsd',
                                                'ST'),
                                               ('MetricTypeType',
                                                'serviceMetrics.xsd',
                                                'ST'),
                                               ('MetricDefinitionType',
                                                'serviceMetrics.xsd',
                                                'CT'),
                                               ('MetricDescriptionType',
                                                'serviceMetrics.xsd',
                                                'CT'),
                                               ('MetricType',
                                                'serviceMetrics.xsd',
                                                'CT'),
                                               ('MetricValueType',
                                                'serviceMetrics.xsd',
                                                'CT'),
                                               ('QueryServiceMetricsListResponseType',
                                                'serviceMetrics.xsd',
                                                'CT'),
                                               ('QueryServiceMetricsResponseType',
                                                'serviceMetrics.xsd',
                                                'CT')]}

__all__ = [
    "AdditionalDataType",
    "AdditionalQueryParamsType",
    "AddressType",
    "AdvanceDataType",
    "AdvancePaymentDataType",
    "AggregateInvoiceLineDataType",
    "AircraftType",
    "AnnulmentDataType",
    "AnnulmentOperationListType",
    "AnnulmentOperationType",
    "AuditDataType",
    "BasicHeaderType",
    "BasicOnlineInvoiceRequestType",
    "BasicOnlineInvoiceResponseType",
    "BasicRequestType",
    "BasicResponseType",
    "BasicResultType",
    "BatchInvoiceType",
    "BusinessValidationResultType",
    "ContractNumbersType",
    "ConventionalInvoiceInfoType",
    "CostCentersType",
    "CryptoType",
    "CustomerCompanyCodesType",
    "CustomerDeclarationType",
    "CustomerInfoType",
    "CustomerTaxNumberType",
    "CustomerVatDataType",
    "DateIntervalParamType",
    "DateTimeIntervalParamType",
    "DealerCodesType",
    "DeliveryNotesType",
    "DetailedAddressType",
    "DetailedReasonType",
    "DieselOilPurchaseType",
    "DiscountDataType",
    "EkaerIdsType",
    "FiscalRepresentativeType",
    "GeneralErrorHeaderResponse",
    "GeneralErrorHeaderResponseType",
    "GeneralErrorResponse",
    "GeneralErrorResponseType",
    "GeneralExceptionResponse",
    "GeneralLedgerAccountNumbersType",
    "GlnNumbersType",
    "InvoiceAnnulment",
    "InvoiceAnnulmentType",
    "InvoiceChainDigestResultType",
    "InvoiceChainDigestType",
    "InvoiceChainElementType",
    "InvoiceChainQueryType",
    "InvoiceData",
    "InvoiceDataResultType",
    "InvoiceDataType",
    "InvoiceDetailType",
    "InvoiceDigestResultType",
    "InvoiceDigestType",
    "InvoiceHeadType",
    "InvoiceLinesType",
    "InvoiceMainType",
    "InvoiceNumberQueryType",
    "InvoiceOperationListType",
    "InvoiceOperationType",
    "InvoiceQueryParamsType",
    "InvoiceReferenceDataType",
    "InvoiceReferenceType",
    "InvoiceType",
    "ItemNumbersType",
    "LineAmountsNormalType",
    "LineAmountsSimplifiedType",
    "LineGrossAmountDataType",
    "LineModificationReferenceType",
    "LineNetAmountDataType",
    "LineType",
    "LineVatDataType",
    "LinesType",
    "ManageAnnulmentRequest",
    "ManageAnnulmentRequestType",
    "ManageAnnulmentResponse",
    "ManageInvoiceRequest",
    "ManageInvoiceRequestType",
    "ManageInvoiceResponse",
    "MandatoryQueryParamsType",
    "MaterialNumbersType",
    "MetricDefinitionType",
    "MetricDescriptionType",
    "MetricType",
    "MetricValueType",
    "NewCreatedLinesType",
    "NewTransportMeanType",
    "NotificationType",
    "NotificationsType",
    "OrderNumbersType",
    "PaymentEvidenceDocumentDataType",
    "PointerType",
    "ProcessingResultListType",
    "ProcessingResultType",
    "ProductCodeType",
    "ProductCodesType",
    "ProductFeeClauseType",
    "ProductFeeDataType",
    "ProductFeeSummaryType",
    "ProductFeeTakeoverDataType",
    "ProjectNumbersType",
    "QueryInvoiceChainDigestRequest",
    "QueryInvoiceChainDigestRequestType",
    "QueryInvoiceChainDigestResponse",
    "QueryInvoiceChainDigestResponseType",
    "QueryInvoiceCheckRequest",
    "QueryInvoiceCheckResponse",
    "QueryInvoiceCheckResponseType",
    "QueryInvoiceDataRequest",
    "QueryInvoiceDataRequestType",
    "QueryInvoiceDataResponse",
    "QueryInvoiceDataResponseType",
    "QueryInvoiceDigestRequest",
    "QueryInvoiceDigestRequestType",
    "QueryInvoiceDigestResponse",
    "QueryInvoiceDigestResponseType",
    "QueryServiceMetricsListResponse",
    "QueryServiceMetricsListResponseType",
    "QueryServiceMetricsResponse",
    "QueryServiceMetricsResponseType",
    "QueryTaxpayerRequest",
    "QueryTaxpayerRequestType",
    "QueryTaxpayerResponse",
    "QueryTaxpayerResponseType",
    "QueryTransactionListRequest",
    "QueryTransactionListRequestType",
    "QueryTransactionListResponse",
    "QueryTransactionListResponseType",
    "QueryTransactionStatusRequest",
    "QueryTransactionStatusRequestType",
    "QueryTransactionStatusResponse",
    "QueryTransactionStatusResponseType",
    "ReferencesToOtherLinesType",
    "RelationQueryDateType",
    "RelationQueryMonetaryType",
    "RelationalQueryParamsType",
    "ShippingDatesType",
    "SimpleAddressType",
    "SoftwareType",
    "SummaryByVatRateType",
    "SummaryGrossDataType",
    "SummaryNormalType",
    "SummarySimplifiedType",
    "SummaryType",
    "SupplierCompanyCodesType",
    "SupplierInfoType",
    "TaxNumberType",
    "TaxpayerAddressItemType",
    "TaxpayerAddressListType",
    "TaxpayerDataType",
    "TechnicalValidationResultType",
    "TokenExchangeRequest",
    "TokenExchangeResponse",
    "TokenExchangeResponseType",
    "TransactionListResultType",
    "TransactionQueryParamsType",
    "TransactionResponseType",
    "TransactionType",
    "UserHeaderType",
    "VatAmountMismatchType",
    "VatRateGrossDataType",
    "VatRateNetDataType",
    "VatRateType",
    "VatRateVatDataType",
    "VehicleType",
    "VesselType"
]
