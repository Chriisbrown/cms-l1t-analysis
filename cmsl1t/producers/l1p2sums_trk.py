from __future__ import print_function
from cmsl1t.energySums import EnergySum, Met
from .base import BaseProducer


class Producer(BaseProducer):

    def __init__(self, inputs, outputs, **kwargs):
        self._expected_input_order = ['et', 'phi']
        super(Producer, self).__init__(inputs, outputs, **kwargs)

    def produce(self, event):

        l1Met = 0
        trkMets = ['L1TrkMET_TrkMet', 'L1TrkMET_CutTrkMet', 'L1TrkMET_MVATrkMet','L1TrkMET_SimTrkMet']
        for trkMet in trkMets:
            if trkMet in self._inputs:
                l1Met = event[trkMet]
                l1MetPhi = event[trkMet + 'Phi']
                break

        trkHts = ['L1TrackJet_TrkJetHt', 'L1TrackJet_CutTrkJetHt', 'L1TrackJet_MVATrkJetHt']
        for trkHt in trkHts:
            if trkHt in self._inputs:
                l1Ht = event[trkHt]
                break

        setattr(event, self._outputs[0] + '_Met', Met(l1Met, l1MetPhi))
        setattr(event, self._outputs[0] + '_MetHF', Met(l1Met, l1MetPhi))
        setattr(event, self._outputs[0] + '_Htt', EnergySum(l1Ht))

        return True
