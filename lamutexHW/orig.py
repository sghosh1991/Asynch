
import da
PatternExpr_2 = da.pat.TuplePattern([da.pat.ConstantPattern('ack'), da.pat.FreePattern('c2'), da.pat.BoundPattern('_BoundPattern7_')])
PatternExpr_4 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern('c2'), da.pat.FreePattern('p')])
PatternExpr_5 = da.pat.TuplePattern([da.pat.ConstantPattern('release'), da.pat.FreePattern(None), da.pat.FreePattern('p')])
PatternExpr_8 = da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.BoundPattern('_BoundPattern33_')])
PatternExpr_9 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.BoundPattern('_BoundPattern43_')])])
import sys

class P(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._PReceivedEvent_0 = []
        self._PReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_2, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_4, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_0]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_5, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_8, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, s, nrequests):
        self.nrequests = nrequests
        self.s = s
        self.q = set()

    def _da_run_internal(self):

        def task():
            self.output('in cs')
        for i in range(self.nrequests):
            self.mutex(task)
        self._send(('done', self.id), self.s)
        p = None

        def UniversalOpExpr_3():
            nonlocal p
            for p in self.s:
                if (not PatternExpr_9.match_iter(self._PReceivedEvent_3, _BoundPattern43_=p)):
                    return False
            return True
        _st_label_27 = 0
        while (_st_label_27 == 0):
            _st_label_27 += 1
            if UniversalOpExpr_3():
                _st_label_27 += 1
            else:
                super()._label('_st_label_27', block=True)
                _st_label_27 -= 1
        self.output('terminating')

    def mutex(self, task):
        super()._label('request', block=False)
        c = self.logical_clock()
        self._send(('request', c, self.id), self.s)
        self.q.add(('request', c, self.id))
        p = c2 = None

        def UniversalOpExpr_0():
            nonlocal p, c2
            for (_ConstantPattern0_, c2, p) in self.q:
                if (_ConstantPattern0_ == 'request'):
                    if (not (((c2, p) == (c, self.id)) or ((c, self.id) < (c2, p)))):
                        return False
            return True
        p = c2 = None

        def UniversalOpExpr_1():
            nonlocal p, c2
            for p in self.s:

                def ExistentialOpExpr_2(p):
                    nonlocal c2
                    for (_, _, (_ConstantPattern16_, c2, _BoundPattern18_)) in self._PReceivedEvent_0:
                        if (_ConstantPattern16_ == 'ack'):
                            if (_BoundPattern18_ == p):
                                if (c2 > c):
                                    return True
                    return False
                if (not ExistentialOpExpr_2(p=p)):
                    return False
            return True
        _st_label_10 = 0
        while (_st_label_10 == 0):
            _st_label_10 += 1
            if (UniversalOpExpr_0() and UniversalOpExpr_1()):
                _st_label_10 += 1
            else:
                super()._label('_st_label_10', block=True)
                _st_label_10 -= 1
        super()._label('critical_section', block=False)
        task()
        super()._label('release', block=False)
        self.q.remove(('request', c, self.id))
        self._send(('release', self.logical_clock(), self.id), self.s)

    def _P_handler_0(self, c2, p):
        self.q.add(('request', c2, p))
        self._send(('ack', self.logical_clock(), self.id), p)
    _P_handler_0._labels = None
    _P_handler_0._notlabels = None

    def _P_handler_1(self, p):
        for x in {('request', c, p) for (_ConstantPattern27_, c, _BoundPattern29_) in self.q if (_ConstantPattern27_ == 'request') if (_BoundPattern29_ == p)}:
            self.q.remove(x)
            break
    _P_handler_1._labels = None
    _P_handler_1._notlabels = None

def main():
    nprocs = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
    nrequests = (int(sys.argv[2]) if (len(sys.argv) > 2) else 1)
    da.config(channel='fifo', clock='Lamport')
    ps = da.new(P, num=nprocs)
    for p in ps:
        da.setup(p, ((ps - {p}), nrequests))
    da.start(ps)
