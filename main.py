import logging
import string
import re
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

import converter

logger = logging.getLogger(__name__)
from_binary_names = ["octal", "decimal", "hexadecimal"]
from_binary_icons = ["octal.png", "decimal.png", "hexadecimal.png"]

from_octal_names = ["binary", "decimal", "hexadecimal"]
from_octal_icons = ["binary.png", "decimal.png", "hexadecimal.png"]

from_decimal_names = ["binary", "octal", "hexadecimal"]
from_decimal_icons = ["binary.png", "octal.png", "hexadecimal.png"]

from_hexadecimal_names = ["binary", "octal", "decimal"]
from_hexadecimal_icons = ["binary.png", "octal.png", "decimal.png"]


class DecimalConverterExtension(Extension):

    def __init__(self):
        logger.info('init Decimal Converter extension')
        super(DecimalConverterExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        rawstr = event.get_argument()
        if rawstr is None or len(rawstr) == 0:
            return RenderResultListAction(items)

        keyword = event.get_keyword()
        result_list = []
        if keyword == extension.preferences["binary_kw"]:
            result_list = converter.convert_from_binary(rawstr)
        elif keyword == extension.preferences["octal_kw"]:
            result_list = converter.convert_from_octal(rawstr)
        elif keyword == extension.preferences["decimal_kw"]:
            result_list = converter.convert_from_decimal(rawstr)
        elif keyword == extension.preferences["hexadecimal_kw"]:
            result_list = converter.convert_from_hexadecimal(rawstr)

        if len(result_list) != 3:
            return RenderResultListAction(items)

        des_l = ', press enter to copy to clipboard.'
        if keyword == extension.preferences["binary_kw"]:
            for i in range(3):
                result = result_list[i]
                icon_str = 'images/' + from_binary_icons[i]
                des_str = from_binary_names[i] + des_l
                items.append(ExtensionResultItem(icon=icon_str,
                                                 name=result,
                                                 description=des_str,
                                                 highlightable=False,
                                                 on_enter=CopyToClipboardAction(result)
                                                 ))
        elif keyword == extension.preferences["octal_kw"]:
            for i in range(3):
                result = result_list[i]
                icon_str = 'images/' + from_octal_icons[i]
                des_str = from_octal_names[i] + des_l
                items.append(ExtensionResultItem(icon=icon_str,
                                                 name=result,
                                                 description=des_str,
                                                 highlightable=False,
                                                 on_enter=CopyToClipboardAction(result)
                                                 ))
        elif keyword == extension.preferences["decimal_kw"]:
            for i in range(3):
                result = result_list[i]
                icon_str = 'images/' + from_decimal_icons[i]
                des_str = from_decimal_names[i] + des_l
                items.append(ExtensionResultItem(icon=icon_str,
                                                 name=result,
                                                 description=des_str,
                                                 highlightable=False,
                                                 on_enter=CopyToClipboardAction(result)
                                                 ))
        elif keyword == extension.preferences["hexadecimal_kw"]:
            for i in range(3):
                result = result_list[i]
                icon_str = 'images/' + from_hexadecimal_icons[i]
                des_str = from_hexadecimal_names[i] + des_l
                items.append(ExtensionResultItem(icon=icon_str,
                                                 name=result,
                                                 description=des_str,
                                                 highlightable=False,
                                                 on_enter=CopyToClipboardAction(result)
                                                 ))

        return RenderResultListAction(items)


if __name__ == '__main__':
    DecimalConverterExtension().run()
