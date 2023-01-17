class Speed:
    def __init__(self, analyst):
        self.analyst = analyst

    def collect(self, url):
        metrics = self.analyst.console_script(url, "return window.performance.timing")
        return metrics

    def front_end(self, url):
        scripts = [
            "return window.performance.timing.navigationStart",
            "return window.performance.timing.domInteractive"
        ]
        output = self.analyst.console_script(url, scripts)
        return output[1] - output[0]

    def back_end(self, url):
        scripts = [
            "return window.performance.timing.navigationStart",
            "return window.performance.timing.domComplete"
        ]
        output = self.analyst.console_script(url, scripts)
        return output[1] - output[0]

"""
window.performance.timing

    https://stackoverflow.com/questions/16808486/explanation-of-window-performance-javascript
    https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/

    connectEnd: 1656577295759                       where the connection is opened network
    connectStart: 1656577295759                     where the request to open a connection is sent to the network
    domComplete: 1656577301558                      when the parser finished its work on the main document, that is when its Document.readyState changes to 'complete' and the corresponding readystatechange event is thrown.
    domContentLoadedEventEnd: 1656577300934         right after all the scripts that need to be executed as soon as possible, in order or not, have been executed
    domContentLoadedEventStart: 1656577300930       right before the parser sent the DOMContentLoaded event, that is right after all the scripts that need to be executed right after parsing has been executed
    domInteractive: 1656577300930                   when the parser finished its work on the main document, that is when its Document.readyState changes to 'interactive' and the corresponding readystatechange event is thrown.
    domLoading: 1656577297661                       when the parser started its work, that is when its Document.readyState changes to 'loading' and the corresponding readystatechange event is thrown
    domainLookupEnd: 1656577295759                  where the domain lookup is finished
    domainLookupStart: 1656577295759                where the domain lookup starts
    fetchStart: 1656577295759                       the browser is ready to fetch the document using an HTTP request. This moment is before the check to any application cache
    loadEventEnd: 1656577301559                     when the load event handler terminated, that is when the load event is completed
    loadEventStart: 1656577301558                   when the load event was sent for the current document
    navigationStart: 1656577295756                  right after the prompt for unload terminates on the previous document in the same browsing context. If there is no previous document, this value will be the same as PerformanceTiming.fetchStart
    redirectEnd: 0                                  the first HTTP redirect ends
    redirectStart: 0                                the first HTTP redirect starts
    requestStart: 1656577295761                     when the browser sent the request to obtain the actual document, from the server or from a cache
    responseEnd: 1656577297651
    responseStart: 1656577297649
    secureConnectionStart: 0
    unloadEventEnd: 1656577297660
    unloadEventStart: 1656577297660
"""