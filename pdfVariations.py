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
r.gROOT.SetBatch(True) # suppress the creation of canvases on the screen... much much faster if over a remote connection
# r.gStyle.SetOptStat(0)
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
xBin = 11
yBin = 26
c1.Print("foo.ps[")
HTbins = [275,325]+ [375+100*i for i in range(6)]
for lower,upper in zip(HTbins,HTbins[1:]+[None]) :
  Text = r.TLatex(0.1,0.92,"PdfOps_%d%s_hist"%(lower,"_%d"%upper if upper else ""))
  Text.SetNDC()
  M0_200_M12_600  = r.TH1D("PdfOpsM0_200_M12_600_%d%s_hist"%(lower,"_%d"%upper if upper else ""),"",4000,0.,0.4)
  M0_500_M12_500  = r.TH1D("PdfOpsM0_500_M12_500_%d%s_hist"%(lower,"_%d"%upper if upper else ""),"",4000,0.,0.4)
  M0_1000_M12_300 = r.TH1D("PdfOpsM0_1000_M12_300_%d%s_hist"%(lower,"_%d"%upper if upper else ""),"",4000,0.,0.4)
  M0_2000_M12_200 = r.TH1D("PdfOpsM0_2000_M12_200_%d%s_hist"%(lower,"_%d"%upper if upper else ""),"",4000,0.,0.4)


  print "PdfOps_%d%s"%(lower,"_%d"%upper if upper else "")
  for i in range(0,41):
    cuts = []
    nocuts = []
    process = ["nn","ns","ng","ss","ll","sb","tb","gg","bb","sg"]
    events = 0
    weighted = []
    nonweighted = []
    processCrossSections = []
    for p in process:
      cuts.append(GetHist(DataSetName = File,folder = "PdfOps_%d%s"%(lower,"_%d"%upper if upper else "") ,
                      hist = "m0_m12_%s_noweight"%(p),col = 1,norm = None ,Legend = "hist",rebin= 2))

      nocuts.append(GetHist(DataSetName = File,folder = "PdfOps_before",
                      hist = "m0_m12_%s_noweight"%(p),col = 1,norm = 1./8. ,Legend = "hist",rebin= 2))

      weighted.append(GetHist(DataSetName = File,folder = "PdfOps_before",
                      hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = 1./8 ,Legend = "hist",rebin= 2))

      nonweighted.append(GetHist(DataSetName = File,folder = "PdfOps_before",
                      hist = "m0_m12_%s_noweight"%(p),col = 1,norm = 1./8. ,Legend = "hist",rebin= 2))

      # Make the process cross sections:
      p_xsec = GetHist(DataSetName = File,folder = "PdfOps_before",
                      hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = 1./8 ,Legend = "hist",rebin= 2)
      p_xsec.Divide(GetHist(DataSetName = File,folder = "PdfOps_before",
                      hist = "m0_m12_%s_noweight"%(p),col = 1,norm = 1./8. ,Legend = "hist",rebin= 2))
      processCrossSections.append(p_xsec)
    # for cut,nocut in zip(cuts,nocuts):
      # events += (cut.GetBinContent(xBin,yBin)/nocut.GetBinContent(xBin,yBin))
    # Make Total Xsection:
    totalXsec =  nloTotalXsecMaker(weighted,nonweighted)
    TotalEff =  NloEffHisto(cuts,nocuts,processCrossSections,totalXsec)

    if i == 0:
      Nevents = Adder(cuts)
      Nevents.Divide(Adder(nocuts))
      c1.SetLogz(r.kFALSE)
      Nevents.Draw("COLZ")
      Nevents.GetZaxis().SetLabelSize(0.02)
      Text = r.TLatex(0.1,0.92,"Nevents in sum of pdfops before ")
      Text.SetNDC()
      Text.Draw("SAME")
      c1.Print("foo.ps")

    # print "cross section of point is ", totalXsec.GetBinContent(xBin,yBin), " M0,M12 (%d,%d)"%(nocuts[0].GetXaxis().GetBinLowEdge(xBin),nocuts[0].GetYaxis().GetBinLowEdge(yBin)), "sum of sigma * N for point is ", trial.GetBinContent(xBin,yBin)

    if i == 0:
      Text = r.TLatex(0.1,0.92,"Eff PdfOps_%d%s_hist M0,M12 = %f%f"%(lower,"_%d"%upper if upper else "", nocuts[0].GetXaxis().GetBinLowEdge(xBin),nocuts[0].GetYaxis().GetBinLowEdge(yBin)))
      Text.SetNDC()
      TotalEff.GetZaxis().SetLabelSize(0.02)
      if lower is 875:
        TotalEff.SetMaximum(0.16)
        TotalEff.SetMinimum(0.0)
      TotalEff.Draw("COLZ")
      c1.SetLogz(r.kFALSE)
      Text.Draw("SAME")
      c1.Print("foo.ps")


    # print "PdfOps_%d%s_hist"%(lower,"_%d"%upper if upper else "") , "events", events
    # e_275.Fill(TotalEff.GetBinContent(xBin,yBin))
    M0_200_M12_600.Fill(TotalEff.GetBinContent(11,31))
    M0_500_M12_500.Fill(TotalEff.GetBinContent(26,26))
    M0_1000_M12_300.Fill(TotalEff.GetBinContent(51,17))
    M0_2000_M12_200.Fill(TotalEff.GetBinContent(91,11))
    # print "Lenght of histogram containers is (cuts,nocuts,xsec) = (%d,%d,%d)"%(len(cuts),len(nocuts),len(xsec))
    # for cut,nocut,xsection in zip(cuts,nocuts,xsec):

    # nom = EffMaker(cuts,nocuts,xsec)
    c1.cd()
    # c1.SetLogz()
    # nom.Draw("COLZ")
    # Text.Draw("SAME")
    # c1.Print("foo.ps")
  # for cut,nocut in zip(cuts,nocuts):
    # print "bin content of M0,M12 (%d,%d) is %f"%(nocut.GetXaxis().GetBinLowEdge(xBin),nocut.GetYaxis().GetBinLowEdge(yBin),nocut.GetBinContent(xBin,yBin))
    # if nocut.GetBinContent(xBin,yBin) > 0: e_275.Fill(cut.GetBinContent(xBin,yBin) /nocut.GetBinContent(xBin,yBin))
  # e_275.Draw("hist")
  M0_200_M12_600.Draw("hist")
  Text = r.TLatex(0.1,0.92,"Eff dist M0,M12 = %d, %d"%(nocuts[0].GetXaxis().GetBinLowEdge(11),nocuts[0].GetYaxis().GetBinLowEdge(31)))
  Text.SetNDC()
  Text.Draw("SAME")
  c1.Print("foo.ps")
  M0_500_M12_500.Draw("hist")
  Text = r.TLatex(0.1,0.92,"Eff dist M0,M12 = %d, %d"%(nocuts[0].GetXaxis().GetBinLowEdge(26),nocuts[0].GetYaxis().GetBinLowEdge(26)))
  Text.SetNDC()
  Text.Draw("SAME")
  c1.Print("foo.ps")
  M0_1000_M12_300.Draw("hist")
  Text = r.TLatex(0.1,0.92,"Eff dist M0,M12 = %d, %d"%(nocuts[0].GetXaxis().GetBinLowEdge(51),nocuts[0].GetYaxis().GetBinLowEdge(17)))
  Text.SetNDC()
  Text.Draw("SAME")
  c1.Print("foo.ps")
  M0_2000_M12_200.Draw("hist")
  Text = r.TLatex(0.1,0.92,"Eff dist M0,M12 = %d, %d"%(nocuts[0].GetXaxis().GetBinLowEdge(91),nocuts[0].GetYaxis().GetBinLowEdge(11)))
  Text.SetNDC()
  Text.Draw("SAME")
  c1.Print("foo.ps")
  totalXsec.GetZaxis().SetLabelSize(0.02)
  totalXsec.Draw("COLZ")
  totalXsec.SetMinimum(0.01)
  totalXsec.SetMaximum(100000.)
  c1.SetLogz()
  Text = r.TLatex(0.1,0.92,"Xsection PdfOps_%d%s_hist"%(lower,"_%d"%upper if upper else ""))
  Text.SetNDC()
  Text.Draw("SAME")
  c1.Print("foo.ps")
  for f in r.gROOT.GetListOfFiles() :f.Close()





# xsec = before_i / before noWeight






c1.Print("foo.ps]")
os.popen("ps2pdf ./foo.ps")










# e_275.GetXaxis().SetRangeUser(0.24,0.28)
