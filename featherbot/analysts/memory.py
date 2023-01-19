class Memory:
    def __init__(self, analyst):
        self.analyst = analyst

    def collect(self, url):
        metrics = self.analyst.console_script(url, "return window.performance.memory")
        return metrics

    def size(self, url):
        return self.analyst.console_script(url, "return window.performance.memory.totalJSHeapSize")