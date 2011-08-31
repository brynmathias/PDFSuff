#!/usr/bin/env python
# encoding: utf-8
"""
pdfVariations.py

Created by Bryn Mathias on 2011-08-22.
Copyright (c) 2011 Imperial College. All rights reserved.
"""
import array
import sys
import os
import ROOT as r
import math
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
TextFile = open("./TextFile.txt",'w')
text200600  = ""
text500500  = ""
text1000300 = ""
text2000200 = ""
# gg_before = GetHist(DataSetName = File,folder = "mSuGraScan_before_scale1" ,hist = "m0_m12_gg_noweight",col = 1,norm = 1./8. ,Legend = "hist",rebin = 2)
# File = r."PDFUncert.root".Open("PDFUncert.root")
# File = r.TFile.Open("PDFUncert.root")
# File = "PDFUncert.root"
# File = "PDFUncert.root"
File = "NNPDF.root"
xBin = 11
yBin = 31
# c1.Print("foo_NNPDF.ps[")
# HTbins = [275,325]+ [375+100*i for i in range(6)]
# for lower,upper in zip(HTbins,HTbins[1:]+[None]) :
#   Text = r.TLatex(0.1,0.92,"PdfOps_%d%s_hist"%(lower,"_%d"%upper if upper else ""))
#   Text.SetNDC()
#   TotalEff = []
#   print "PdfOps_%d%s"%(lower,"_%d"%upper if upper else "")
#   VarList = []
#   for i in range(0,2):
#     print "I is  %d"%(i)
#     cuts = []
#     nocuts = []
#     process = ["nn","ns","ng","ss","ll","sb","tb","gg","bb","sg"]
#     events = 0
#     weighted = []
#     nonweighted = []
#     processCrossSections = []
#     for p in process:
#       print "Getting hist PdfOps_%d%s"%(lower,"_%d"%upper if upper else "")
#       cuts.append(GetHist(DataSetName = File,folder = "PdfOps_%d%s"%(lower,"_%d"%upper if upper else "") ,
#                       hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = None ,Legend = "hist",rebin= 2))
#
#       nocuts.append(GetHist(DataSetName = File,folder = "PdfOps_before",
#                       hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = 1./8. ,Legend = "hist",rebin= 2))
#
#       weighted.append(GetHist(DataSetName = File,folder = "PdfOps_before",
#                       hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = 1./8 ,Legend = "hist",rebin= 2))
#
#       nonweighted.append(GetHist(DataSetName = File,folder = "PdfOps_before",
#                       hist = "m0_m12_%s_noweight"%(p),col = 1,norm = 1./8. ,Legend = "hist",rebin= 2))
#
#       # Make the process cross sections:
#       p_xsec = GetHist(DataSetName = File,folder = "PdfOps_before",
#                       hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = 1./8 ,Legend = "hist",rebin= 2)
#       p_xsec.Divide(GetHist(DataSetName = File,folder = "PdfOps_before",
#                       hist = "m0_m12_%s_noweight"%(p),col = 1,norm = 1./8. ,Legend = "hist",rebin= 2))
#       processCrossSections.append(p_xsec)
#     # for cut,nocut in zip(cuts,nocuts):
#       # events += (cut.GetBinContent(xBin,yBin)/nocut.GetBinContent(xBin,yBin))
#     # Make Total Xsection:
#     totalXsec =  nloTotalXsecMaker(weighted,nonweighted)
#     totalXsec.Draw("COLZ")
#     Text = r.TLatex(0.1,0.92,"Cross section Variation %d"%(i))
#     Text.SetNDC()
#     Text.Draw("SAME")
#     TotalEff.append(NloEffHisto(cuts,nocuts,processCrossSections,totalXsec))
#
#
#
#
#       # Text = r.TLatex(0.1,0.92,"Eff PdfOps_%d%s_hist M0,M12 = %f%f"%(lower,"_%d"%upper if upper else "", nocuts[0].GetXaxis().GetBinLowEdge(xBin),nocuts[0].GetYaxis().GetBinLowEdge(yBin)))
#       # Text.SetNDC()
#       # TotalEff.GetZaxis().SetLabelSize(0.02)
#       # # if lower is 875:
#       # TotalEff.SetNdivisions(510,"Z")
#       # TotalEff.SetMaximum(0.16)
#       # TotalEff.SetMinimum(0.0)
#       # TotalEff.Draw("COLZ")
#       # c1.SetLogz(r.kFALSE)
#       # Text.Draw("SAME")
#       # c1.Print("foo_NNPDF.ps")
#   varIdx = 0
#   RMSHist = TotalEff[0].Clone()
#   print "Length of var Histlist" , len(VarList)
#   for x in range(0,RMSHist.GetNbinsX()):
#     for y in range(0,RMSHist.GetNbinsY()):
#       hist = r.TH1D("%d_%d"%(x,y),"%d_%d"%(x,y),10000,0.,1.)
#       for EffPlot in TotalEff: hist.Fill(EffPlot.GetBinContent(x,y))
#       RMSHist.SetBinContent(x,y,hist.GetRMS())
#
#
#   # c1.Print("foo_NNPDF.ps")
#   Text = r.TLatex(0.1,0.92,"RMS HIST %d%s_hist "%(lower,"_%d"%upper if upper else ""))
#   Text.SetNDC()
#
#   RMSHist.GetZaxis().SetLabelSize(0.02)
#   RMSHist.Draw("COLZ")
#   Text.Draw("SAME")
#   c1.Print("foo_NNPDF.ps")
#   for f in r.gROOT.GetListOfFiles() : f.Close()
#
#
# c1.Print("foo_NNPDF.ps]")
# os.popen("ps2pdf ./foo_NNPDF.ps")
#








#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
c1.Print("bar_NNPDF.ps[")
page = 0
# Now we make plot set 2 - variations in HT dependant binning.
# First make central bin - 0th variation
HTbins = [275,325]+ [375+100*i for i in range(6)]
Default = r.TH1D("Default","Default",8,array.array('d',HTbins+[3000]))
Default.SetLineColor(2)
HTHistoList = []
for i in range(0,101):
  Text = r.TLatex(0.1,0.92,"PdfOps_Variation_%f"%(i))
  Text.SetNDC()
  Varied =  r.TH1D("Variation_%f"%(i),"Variation_%f"%(i),8,array.array('d',HTbins+[3000]))
  bin = 0
  for lower,upper in zip(HTbins,HTbins[1:]+[None]) :
    bin += 1
    print "PdfOps_%d%s"%(lower,"_%d"%upper if upper else "")
    cuts = []
    nocuts = []
    process = ["nn","ns","ng","ss","ll","sb","tb","gg","bb","sg"]
    events = 0
    weighted = []
    nonweighted = []
    processCrossSections = []
    for p in process:
      # print "m0_m12_%s_%d"%(p,i)
      cuts.append(GetHist(DataSetName = File,folder = "PdfOps_%d%s"%(lower,"_%d"%upper if upper else "") ,
                      hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = None ,Legend = "hist",rebin= 2))

      nocuts.append(GetHist(DataSetName = File,folder = "PdfOps_before",
                      hist = "m0_m12_%s_%d"%(p,i),col = 1,norm = 1./8. ,Legend = "hist",rebin= 2))

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
    if i is 0: Default.SetBinContent(bin, TotalEff.GetBinContent(xBin,yBin))
    print "Varied Cross section is ", TotalEff.GetBinContent(xBin,yBin) , "in bin", Default.GetBinLowEdge(bin)
    Varied.SetBinContent(bin, TotalEff.GetBinContent(xBin,yBin))

  Default.GetXaxis().SetRangeUser(0.,900.)
  HTHistoList.append(Varied)
  Default.Draw("hist")
  Varied.SetLineColor(4)
  Varied.Draw("SAMEHIST")
  Text.Draw("SAME")
  # c1.Print("bar_NNPDF.ps")
  Ratio = Default.Clone()
  Ratio.Divide(Varied)
  Ratio.Draw("HIST")
  # c1.Print("bar_NNPDF.ps")
  # print "Page %d written"%(page)
  # page += 1
  for f in r.gROOT.GetListOfFiles() : f.Close()



c1.Clear()
c1.Print("bar_NNPDF.ps")
newDefault = Default.Clone()
for bin in range(0,newDefault.GetNbinsX()+1):
  a = r.TH1D("tmp","tmp",10000,0.,1.)
  for h in HTHistoList:
    print h.GetBinContent(bin) , "BIN CONETENT OF TEM HIST",h.GetBinLowEdge(bin)
    a.Fill(h.GetBinContent(bin))
    # a.Draw("hist")
    # c1.Print("bar_NNPDF.ps")
  print "RMS OF TMP HIST", a.GetRMS()
  newDefault.SetBinError(bin,a.GetRMS())
  print "DEFAULT HISTO BIN CONTENT = " , a.GetBinContent(bin)
newDefault.Draw("")
theFile =r.TFile("NNPDF_output_200_600.root", "RECREATE");
theFile.cd()
newDefault.Write()
theFile.Write()
theFile.Close()
c1.Print("bar_NNPDF.ps")
for f in r.gROOT.GetListOfFiles() :f.Close()
c1.Print("bar_NNPDF.ps]")
os.popen("ps2pdf ./bar_NNPDF.ps")
#
#
#
#
#
#
#
#
#
# # e_275.GetXaxis().SetRangeUser(0.24,0.28)
