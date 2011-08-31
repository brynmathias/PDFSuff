#!/usr/bin/env python
# encoding: utf-8
"""
testReader.py

Created by Bryn Mathias on 2011-08-28.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingstuff import *

# leg = r.TLegend(0.1, 0.4, 0.6, 1.0)
# leg.SetShadowColor(0)
# leg.SetBorderSize(0)
# leg.SetFillStyle(4100)
# leg.SetFillColor(0)
# leg.SetLineColor(0)
# leg.SetShadowColor(0)
# leg.SetBorderSize(0)
# leg.SetFillStyle(4100)
# leg.SetFillColor(0)
# leg.SetLineColor(0)


CTEQ = GetHist(DataSetName = "CTEQ_output.root",folder = None ,hist = "Default",col = 1 ,norm = None ,Legend = "CTEQ 6.1", rebin = None)
MSTW = GetHist(DataSetName = "MSTW_output.root",folder = None ,hist = "Default",col = 2 ,norm = None ,Legend = "MSTW 2006 NLO 68%", rebin = None)
NNPDF = GetHist(DataSetName= "NNPDF_outpu.root",folder = None ,hist = "Default",col = 3 ,norm = None ,Legend = "NNPDF", rebin = None)
r.gStyle.SetOptStat(000000)


CTEQ.SetTitle("Comparison of central Values for the 3 PDF sets, M0 = 200, M12 = 600")
c1 = r.TCanvas("canvas","canname",1400,1200)

c1.cd()
r.gPad.SetTicky()
CTEQ.SetMinimum(0.)
CTEQ.Draw("h")
MSTW.Draw("hsame")
NNPDF.Draw("hsame")
leg.Draw("same")
c1.SaveAs("PDFVarComp_200_600.pdf")

c1.Clear()
a = CTEQ.Clone()
a.SetMinimum(0.)
a.SetTitle("Cteq 6.1 / NNPDF")
a.Divide(NNPDF)
a.Draw("h")
c1.SaveAs("CteqOvNNPDF_200_600.pdf")
b = CTEQ.Clone()
b.SetTitle("Cteq 6.1 / MSTW")
b.SetMinimum(0.)
b.Divide(MSTW)
b.Draw("h")
c1.SaveAs("CteqOvMSTW_200_600.pdf")
