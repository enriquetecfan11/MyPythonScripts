#!/usr/bin/env python
# coding=utf-8


from fastkml import kml
import os
import time
import optparse


class wiglekml:
    def __init__(self):
        # self.networks={}
        self.outputname = ""
        self.target = None
        self.disable_names = False
        self.newKml = None

    def main(self):
        usage = self.main_usage()
        parser = optparse.OptionParser(usage)
        parser.add_option(
            "-o", dest="outputname",
            help="Filename without extension")

        (options, args) = parser.parse_args()

        # Input
        if len(args) > 0:
            for filename in args:
                if os.path.isdir(filename):
                    self.parse_dir(filename)
                elif os.path.isfile(filename):
                    self.parse(filename)
                else:
                    print("Invalid name: %s" % filename)
        if options.outputname is None:
            print("Output name not defined, try '-h'")
        else:
            self.outputname = options.outputname + ".kml"
            print("Outputfile: %s" % self.outputname)

        print("")

        if self.outputname != "":
            with open(self.outputname, 'wt') as outFile:
                outFile.write(self.newKml.to_string())

    def parse(self, filename):

        with open(filename, 'rt') as inFile:
            ns = '{http://www.opengis.net/kml/2.2}'

            doc = inFile.read()
            k = kml.KML()
            k.from_string(doc)

            if self.newKml is None:
                self.newKml = kml.KML()
                newDoc = kml.Document(
                    ns, 'docid', 'Filtered Networks',
                    'Networks in Folders by Encryption')
                self.newKml.append(newDoc)
                unknown = kml.Folder(
                    ns, 'unknown', 'Unknown:', 'Unknown Networks')
                unencrypted = kml.Folder(
                    ns, 'unencrypted', 'Unencrypted:', 'Unencrypted Networks')
                wep = kml.Folder(ns, 'wep', 'WEP:', 'WEP Networks')
                wpa = kml.Folder(ns, 'wpa', 'WPA:', 'WPA Networks')
                wpa2 = kml.Folder(ns, 'wpa2', 'WPA2:', 'WPA2 Networks')
                wpa3 = kml.Folder(ns, 'wpa3', 'WPA3:', 'WPA3 Networks')

                newDoc.append(unknown)
                newDoc.append(unencrypted)
                newDoc.append(wep)
                newDoc.append(wpa)
                newDoc.append(wpa2)
                newDoc.append(wpa3)
            else:
                rootFeatures = list(self.newKml.features())
                newDoc = rootFeatures[0]
                folders = list(newDoc.features())
                for folder in folders:
                    if folder.name == "Unknown:":
                        unknown = folder

                    if folder.name == "Unencrypted:":
                        unencrypted = folder

                    if folder.name == "WEP:":
                        wep = folder

                    if folder.name == "WPA:":
                        wpa = folder

                    if folder.name == "WPA2:":
                        wpa2 = folder

                    if folder.name == "WPA3:":
                        wpa3 = folder

            features = list(k.features())  # document level item

            print(
                "%s: contains %d base feature(s)" % (filename, len(features)))
            subfeatures = list(features[0].features())
            placemarks = []

            if len(subfeatures) <= 3:
                print("20190330 Upload file format check...")
                for feature in subfeatures:
                    if feature.name == 'Wifi Networks':
                        print("...confirmed.")
                        placemarks = list(feature.features())
                if placemarks is None:
                    print("...unable to confirm.")
                    # ALIBI: falling back to traditional processing
                    list(features[0].features())
            else:
                print("2016 Upload KML format detected")
                placemarks = list(features[0].features())

            if placemarks is None:
                print("Null placemarks. No categorization possible.")
            else:
                for placemark in placemarks:
                    if "Encryption: None" in placemark.description:
                        unencrypted.append(placemark)

                    elif "Encryption: Unknown" in placemark.description:
                        unknown.append(placemark)

                    elif "Encryption: WPA3" in placemark.description:
                        wpa3.append(placemark)

                    elif "Encryption: WPA2" in placemark.description:
                        wpa2.append(placemark)

                    elif "Encryption: WPA" in placemark.description:
                        wpa.append(placemark)

                    elif "Encryption: WEP" in placemark.description:
                        wep.append(placemark)

            print("unencrypted: %d" % len(list(unencrypted.features())))
            print("unknown: %d" % len(list(unknown.features())))
            print("wep: %d" % len(list(wep.features())))
            print("wpa: %d" % len(list(wpa.features())))
            print("wpa2: %d" % len(list(wpa2.features())))
            print("wpa3: %d" % len(list(wpa3.features())))

    def main_usage(self):
        return """
python kml_filter.py [options] [file1] [file2] [dir1] [dir2] [...]
./kml_filter.py [options] [dir1] [dir2] [file1] [file2] [...]

Example:
python kml_filter.py -o combinedoutput somefile.netxml /mydir"""

    def parse_dir(self, parsedir):
        """Parse all files in a directory
        """
        print("Parse .kml files in Directory:", parsedir)
        starttime = time.time()
        files = 0
        if not parsedir.endswith(os.sep):
            parsedir += os.sep
        for filename in os.listdir(parsedir):
            if os.path.splitext(filename)[1] == ".kml":
                self.parse(parsedir + filename)
                files += 1

if __name__ == "__main__":
    converter = wiglekml()
    converter.main()
