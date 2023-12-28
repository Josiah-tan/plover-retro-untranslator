#!/usr/bin/env python

from typing import List
import itertools
from plover.translation import Translator, Stroke, Translation
from plover.formatting import RetroFormatter
import re

def flatten(x: List[List]) -> List:
    return list(itertools.chain.from_iterable(x))

SHOW_WHITESPACE = str.maketrans({'\n': '\\n', '\r': '\\r', '\t': '\\t'})

historical_translations = []

def expandFormatting(format_string, items): 
    # thanks for this rabbit growth!
    def replace(matchobj):
        width, letter = matchobj.groups()
        width = 0 if not width else int(width)
        return items.get(letter, '').ljust(width)
    return re.sub(r'%(\d*)(.)', replace, format_string)

def formatDefined(raw_string):
    processed_string = re.sub("([{}])", r"\\\1", raw_string)
    return processed_string

def extract_number_key(stroke):
    return_string = stroke.rtfcre
    if stroke.has_digit():
        return_string = "#" + (stroke - Stroke("#")).rtfcre
    return return_string;

def retro_untranslator(translator: Translator, stroke: Stroke, cmdline: str):
    formatting = cmdline
    all_translations = translator.get_state().translations
    affected_translation_cnt = len(list(
        itertools.takewhile(
            lambda x: x.strokes[-1] == stroke,
            reversed(all_translations)
        )
    ))
    affected_translations = all_translations[-(affected_translation_cnt + 1):]
    affected_strokes = flatten([x.strokes for x in affected_translations])
    raw_steno = "/".join([extract_number_key(x) for x in reversed(list(itertools.dropwhile(
        lambda x: x == stroke,
        reversed(affected_strokes)
    )))])
    if len(affected_translations) >= 1:
        affected_english = affected_translations[0]
        global historical_translations
        if affected_translation_cnt:
            historical_translations = [affected_english] + historical_translations 
        else:
            historical_translations = [affected_english]
        try:
            defined = formatDefined(' '.join(translation.english.translate(SHOW_WHITESPACE) for translation in historical_translations))
            translated = ''.join(reversed(list(RetroFormatter(historical_translations).iter_last_fragments())))
        except:
            defined = translated = raw_steno
            print("no available translation")
    else:
        defined = ""
        translated = ""
    
    items = {
        'r': raw_steno,
        'T': translated,
        'D': defined,
        '%': '%'}
    formatted_result = expandFormatting(formatting, items)
    my_trans = Translation(affected_strokes + [stroke], formatted_result)
    my_trans.replaced = affected_translations
    translator.translate_translation(my_trans)
