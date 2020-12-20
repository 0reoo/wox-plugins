from wox import Wox
import time
import win32clipboard as wc
import win32con


class Main(Wox):

    def query(self, query):
        query = str(query).strip(' ')
        if query == "":
            title = str(int(time.time()))
        else:
            if query.isdigit() and len(query) == 10:
                title = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(query)))
            else:
                date_split = query[4:5]
                time_split = ""
                _format = ""
                if len(query) > 13:
                    time_split = query[13:14]
                if len(query) == 10:
                    _format = "%Y{}%m{}%d".format(date_split, date_split)
                elif len(query) == 13:
                    _format = "%Y{}%m{}%d %H".format(date_split, date_split)
                elif len(query) == 16:
                    _format = "%Y{}%m{}%d %H{}%M".format(date_split, date_split, time_split)
                elif len(query) == 19:
                    _format = "%Y{}%m{}%d %H{}%M{}%S".format(date_split, date_split, time_split, time_split)
                title = str(int(time.mktime(time.strptime(query, _format))))
        return [{
            "Title": title,
            "SubTitle": "copy to clipboard",
            "IcoPath": "Images/logo.png",
            "ContextData": "ctxData",
            "JsonRPCAction": {
                "method": "copy",
                "parameters": [title],
                "dontHideAfterAction": False
            }
        }]

    def copy(self, result):
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(win32con.CF_UNICODETEXT, result)
        wc.CloseClipboard()

    def context_menu(self, data):
        results = [{
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath": "Images/app.ico"
        }]
        return results


if __name__ == "__main__":
    Main()
