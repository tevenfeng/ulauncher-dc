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
from_binary_icons = ["octal.png", "decimal.png", "hexadecimal.png"]
from_octal_icons = ["binary.png", "decimal.png", "hexadecimal.png"]
from_decimal_icons = ["binary.png", "octal.png", "hexadecimal.png"]
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
        if keyword == "bin":
            result_list = converter.convert_from_binary(rawstr)
        elif keyword == "oct":
            result_list = converter.convert_from_octal(rawstr)
        elif keyword == "dc":
            result_list = converter.convert_from_decimal(rawstr)
        elif keyword == "hex":
            result_list = converter.convert_from_hexadecimal(rawstr)

        if len(result_list) != 3:
            return RenderResultListAction(items)

        if keyword == "bin":
            for i in range(3):
                result = result_list[i]
                icon_str = 'images/' + from_binary_icons[i]
                items.append(ExtensionResultItem(icon=icon_str,
                                                 name=result,
                                                 description='Chars',
                                                 highlightable=False,
                                                 on_enter=CopyToClipboardAction(result)
                                                 ))
        elif keyword == "oct":
            for i in range(3):
                result = result_list[i]
                icon_str = 'images/' + from_octal_icons[i]
                items.append(ExtensionResultItem(icon=icon_str,
                                                 name=result,
                                                 description='Chars',
                                                 highlightable=False,
                                                 on_enter=CopyToClipboardAction(result)
                                                 ))
        elif keyword == "dc":
            for i in range(3):
                result = result_list[i]
                icon_str = 'images/' + from_decimal_icons[i]
                items.append(ExtensionResultItem(icon=icon_str,
                                                 name=result,
                                                 description='Chars',
                                                 highlightable=False,
                                                 on_enter=CopyToClipboardAction(result)
                                                 ))
        elif keyword == "hex":
            for i in range(3):
                result = result_list[i]
                icon_str = 'images/' + from_hexadecimal_icons[i]
                items.append(ExtensionResultItem(icon=icon_str,
                                                 name=result,
                                                 description='Chars',
                                                 highlightable=False,
                                                 on_enter=CopyToClipboardAction(result)
                                                 ))

        return RenderResultListAction(items)


if __name__ == '__main__':
    DecimalConverterExtension().run()
