#!/usr/bin/python

import sys


def main(argv):
    ir = """
    partial alphanumeric_keys
    xkb_symbols "bita" {

        name[Group1]= "Persian (Bita)";

        include "ir(bita_basic)"

        include "nbsp(zwnj2nb3nnb4)"
        include "level3(ralt_switch)"
    };

    partial alphanumeric_keys
    xkb_symbols "bita_keypad" {
        name[Group1]= "Persian (Bita with Persian Keypad)";

        include "ir(bita_basic)"
        include "ir(pes_part_keypad)"

        include "nbsp(zwnj2nb3nnb4)"
        include "level3(ralt_switch)"
    };

    partial hidden alphanumeric_keys
    xkb_symbols "bita_basic" {

        // Persian digits
        key <TLDE> { [ asciitilde, division, grave ] };
        key <AE01> { [ Farsi_1, exclam, quoteleft ] };
        key <AE02> { [ Farsi_2, 0x100066c, at ] };
        key <AE03> { [ Farsi_3, 0x100066b, numbersign ] };
        key <AE04> { [ Farsi_4, 0x100fdfc, dollar ] };
        key <AE05> { [ Farsi_5, 0x100066a, percent ] };
        key <AE06> { [ Farsi_6, multiply, asciicircum ] };
        key <AE07> { [ Farsi_7, ampersand, ampersand ] };
        key <AE08> { [ Farsi_8, asterisk, enfilledcircbullet ] };
        key <AE09> { [ Farsi_9, parenright, 0x100200e ] };
        key <AE10> { [ Farsi_0, parenleft, 0x100200f ] };
        key <AE11> { [ minus, Arabic_tatweel, underscore ] };
        key <AE12> { [ equal, plus, 0x1002212 ] };

        // Persian letters and symbols
        key <AD01> { [ Arabic_hah, Arabic_sukun, degree ] };
        key <AD02> { [ Arabic_keheh, Arabic_fathatan, Arabic_kaf ] };
        key <AD03> { [ Arabic_teh, Arabic_kasratan, 0x13a4 ] };
        key <AD04> { [ Arabic_feh, Arabic_dammatan, VoidSymbol ] };
        key <AD05> { [ Arabic_qaf, Arabic_superscript_alef, VoidSymbol ] };
        key <AD06> { [ Arabic_sad, 0x1000653, VoidSymbol ] };
        key <AD07> { [ Arabic_khah, Arabic_damma, VoidSymbol ] };
        key <AD08> { [ Arabic_beh, Arabic_kasra, VoidSymbol ] };
        key <AD09> { [ Arabic_seen, Arabic_fatha, VoidSymbol ] };
        key <AD10> { [ Arabic_jeem, Arabic_shadda, VoidSymbol ] };
        key <AD11> { [ Arabic_ghain, braceright, VoidSymbol ] };
        key <AD12> { [ Arabic_zah, braceleft, VoidSymbol ] };

        key <CAPS> { [ 0x100200c, 0x100200d, VoidSymbol ] };
        key <AC01> { [ Arabic_waw, Arabic_hamza, 0x100202d ] };
        key <AC02> { [ Arabic_ra, Arabic_jeh, 0x100202e ] };
        key <AC03> { [ Arabic_alef, guillemotright, 0x100202c ] };
        key <AC04> { [ Arabic_noon, guillemotleft, 0x100202a ] };
        key <AC05> { [ Arabic_lam, bracketright, 0x100202b ] };
        key <AC06> { [ Arabic_sheen, bracketleft, VoidSymbol ] };
        key <AC07> { [ Arabic_heh, Arabic_hamza_above, Arabic_tehmarbuta ] };
        key <AC08> { [ Farsi_yeh, Arabic_hamzaonyeh, Arabic_yeh ] };
        key <AC09> { [ Arabic_meem, colon, VoidSymbol ] };
        key <AC10> { [ Arabic_dal, Arabic_semicolon, semicolon ] };
        key <AC11> { [ Arabic_thal, apostrophe, VoidSymbol ] };
        key <BKSL> { [ Arabic_theh, quotedbl, VoidSymbol ] };

        key <LSGT> { [ Arabic_jeh, VoidSymbol, VoidSymbol ] };
        key <AB01> { [ Arabic_tcheh, Arabic_hamzaonwaw, VoidSymbol ] };
        key <AB02> { [ Arabic_peh, Arabic_hamzaunderalef, VoidSymbol ] };
        key <AB03> { [ Arabic_maddaonalef, Arabic_hamzaonalef, VoidSymbol ] };
        key <AB04> { [ Arabic_zain, slash, 0x100fd3e ] };
        key <AB05> { [ Arabic_tah, backslash, 0x100fd3f ] };
        key <AB06> { [ Arabic_ain, bar, VoidSymbol ] };
        key <AB07> { [ Arabic_gaf, numbersign, ellipsis ] };
        key <AB08> { [ Arabic_comma, less, comma ] };
        key <AB09> { [ period, greater, VoidSymbol ] };
        key <AB10> { [ Arabic_dad, Arabic_question_mark, question ] };
    };
    """

    lst = """  bita            ir: Persian (Bita)
      bita_keypad     ir: Persian (Bita with Persian Keypad)
    """

    xml= """        <variant>
              <configItem>
                <name>bita</name>
                <description>Persian (Bita)</description>
              </configItem>
            </variant>
            <variant>
              <configItem>
                <name>bita_keypad</name>
                <description>Persian (Bita with Persian Keypad)</description>
              </configItem>
            </variant>
    """


    f = open(argv+"/X11/xkb/symbols/ir", 'a')
    f.write(ir)
    f.close()
    print("writing ir")

    f = open(argv+"/X11/xkb/rules/evdev.lst", "r")
    contents = f.readlines()
    f.close()

    index = 1
    for c in contents:
        if "pes_keypad" in c:
            break
        else:
            index = index+1

    contents.insert(index, lst)

    f = open(argv+"/X11/xkb/rules/evdev.lst", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    print("writing lst")

    f = open(argv+"/X11/xkb/rules/evdev.xml", "r")
    contents = f.readlines()
    f.close()

    index = 4
    for c in contents:
        if "pes_keypad" in c:
            break
        else:
            index = index+1

    contents.insert(index, xml)

    f = open(argv+"/X11/xkb/rules/evdev.xml", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    print("writing xml")
    print("All done")


if __name__ == "__main__":
   main(sys.argv[1])



