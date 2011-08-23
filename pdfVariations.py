#!/usr/bin/env python
# encoding: utf-8
"""
pdfVariations.py

Created by Bryn Mathias on 2011-08-22.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
import ROOT as r
from plottingstuff import *
from plottingstuff import EffMaker
leg = r.TLegend(0.1, 0.4, 0.6, 1.0)
leg.SetShadowColor(0)
leg.SetBorderSize(0)
leg.SetFillStyle(4100)
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.SetShadowColor(0)
leg.SetBorderSize(0)
leg.SetFillStyle(4100)
leg.SetFillColor(0)
leg.SetLineColor(0)

c1 = r.TCanvas("canvas","canname",1400,1200)
closeList = []
# NoScale = GetHist(DataSetName = "AK5Calo_mSUGRA_m0_20to2000_m12_20to760_tanb_10andA0_0_7TeV_Pythia6Z_Summer11_PU_S4_START42_V11_FastSim_v1_Had_100.root",folder = "mSuGraScan_before_scale1" ,hist = "m0_m12_gg_",col = 1,norm = None ,Legend = "hist")

# gg_before = GetHist(DataSetName = File,folder = "mSuGraScan_before_scale1" ,hist = "m0_m12_gg_noweight",col = 1,norm = 1./8. ,Legend = "hist",rebin = 2)
# File = r."PDFUncert.root".Open("PDFUncert.root")
File = "PDFUncert.root"
xBin = 10
yBin = 25
c1.Print("foo.ps[")
HTbins = [275,325]+ [375+100*i for i in range(6)]
for lower,upper in zip(HTbins,HTbins[1:]+[None]) :
  Text = r.TLatex(0.1,0.9,"PdfOps_%d%s_hist"%(lower,"_%d"%upper if upper else ""))
  Text.SetNDC()

  e_275 = r.TH1D("PdfOps_%d%s_hist"%(lower,"_%d"%upper if upper else ""),"PdfOps_Hist%d%s"%(lower,"_%d"%upper if upper else ""),1000,0.,0.1)
  print "PdfOps_%d%s"%(lower,"_%d"%upper if upper else "")
  for i in range(0,45):
    cuts = []
    nocuts = []
    process = ["nn","ns","ng","ss","ll","sb","tb","gg","bb","sg"]
    xsec = []
    for p in process:
      cuts.append(GetHist(DataSetName = File,folder = "PdfOps_%d%s"%(lower,"_%d"%upper if upper else "") ,
                      hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = None ,Legend = "hist",rebin= 2))

      nocuts.append(GetHist(DataSetName = File,folder = "PdfOps_before",
                      hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = None ,Legend = "hist",rebin= 2))
      # a = GetHist(DataSetName = File,folder = "PdfOps_before",
      #                 hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = None ,Legend = "hist",rebin= 2)
      # b = GetHist(DataSetName = File,folder = "PdfOps_before",
      #                 hist = "m0_m12_%s_noweight"%(p),col = 1,norm = None ,Legend = "hist",rebin= 2)
      # xsec.append(a.Divide(b))
    print "Lenght of histogram containers is (cuts,nocuts,xsec) = (%d,%d,%d)"%(len(cuts),len(nocuts),len(xsec))
    for cut,nocut,xsection in zip(cuts,nocuts,xsec):

    # nom = EffMaker(cuts,nocuts,xsec)
    c1.cd()
    # c1.SetLogz()
    nom.Draw("COLZ")
    Text.Draw("SAME")
    c1.Print("foo.ps")
  for cut,nocut in zip(cuts,nocuts):
    print "bin content of M0,M12 (%d,%d) is %f"%(nocut.GetXaxis().GetBinLowEdge(xBin),nocut.GetYaxis().GetBinLowEdge(yBin),nocut.GetBinContent(xBin,yBin))
    if nocut.GetBinContent(xBin,yBin) > 0: e_275.Fill(cut.GetBinContent(xBin,yBin) /nocut.GetBinContent(xBin,yBin))
  e_275.Draw("hist")
  c1.Print("foo.ps")
  for f in r.gROOT.GetListOfFiles() :f.Close()










c1.Print("foo.ps]")
os.popen("ps2pdf ./foo.ps")










# e_275.GetXaxis().SetRangeUser(0.24,0.28)
