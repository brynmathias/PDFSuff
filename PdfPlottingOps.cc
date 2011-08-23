#include "AlphaT.hh"
#include "CommonOps.hh"
#include "EventData.hh"
#include "GenMatrixBin.hh"
#include "Jet.hh"
#include "KinSuite.hh"
#include "Lepton.hh"
#include "Math/VectorUtil.h"
#include "Photon.hh"
#include "TH1D.h"
#include "TH2D.h"
#include "Types.hh"
#include <sstream>
#include <string>
#include <iomanip>
#include "NLOTools.hh"
#include <strstream>
#include <iostream>
#include <fstream>

#include "PdfPlottingOps.hh"
#include "JetData.hh"
#include "CommonOps.hh"

#include "LHAPDF/LHAPDF.h"


using namespace Operation;



PDFPlottingOps::PDFPlottingOps( const Utils::ParameterSet& ps ) :
dirName_( ps.Get<std::string>("DirectoryName")),
  xBins_(ps.Get<int>("xBins")),
  xLow_(ps.Get<double>("xLow")),
  xHigh_(ps.Get<double>("xHigh")),
  yBins_(ps.Get<int>("yBins")),
  yLow_(ps.Get<double>("yLow")),
  yHigh_(ps.Get<double>("yHigh")),
  zBins_(ps.Get<int>("zBins")),
  zLow_(ps.Get<double>("zLow")),
  zHigh_(ps.Get<double>("zHigh")),
  verbose_(ps.Get<bool>("verbose")),
  M0_ (ps.Get<std::vector<double> >("NLO.M0")),
  M12_(ps.Get<std::vector<double> >("NLO.M12")),
  NG_ (ps.Get<std::vector<double> >("NLO.ng")),
  NS_ (ps.Get<std::vector<double> >("NLO.ns")),
  NN_ (ps.Get<std::vector<double> >("NLO.nn")),
  LL_ (ps.Get<std::vector<double> >("NLO.ll")),
  SB_ (ps.Get<std::vector<double> >("NLO.sb")),
  SS_ (ps.Get<std::vector<double> >("NLO.ss")),
  TB_ (ps.Get<std::vector<double> >("NLO.tb")),
  BB_ (ps.Get<std::vector<double> >("NLO.bb")),
  GG_ (ps.Get<std::vector<double> >("NLO.gg")),
  SG_ (ps.Get<std::vector<double> >("NLO.sg"))
{
  // std::map< std::pair<int, int>, std::vector<double> > M0_M12_NLO_;
  for(size_t i = 0; i < M0_.size(); ++i)
  {
    std::vector<double> nloVec;
    nloVec.clear();
    nloVec.push_back(NG_[i]);
    nloVec.push_back(NS_[i]);
    nloVec.push_back(NN_[i]);
    nloVec.push_back(LL_[i]);
    nloVec.push_back(SB_[i]);
    nloVec.push_back(SS_[i]);
    nloVec.push_back(TB_[i]);
    nloVec.push_back(BB_[i]);
    nloVec.push_back(GG_[i]);
    nloVec.push_back(SG_[i]);
    M0_M12_NLO_.insert( make_pair(make_pair(int(M0_[i]), int(M12_[i]) ) , nloVec ));
  }
}




PDFPlottingOps::~PDFPlottingOps(){}


void PDFPlottingOps::Start( Event::Data& ev ) {



  initDir( ev.OutputFile(), dirName_.c_str() );

  BookHistos();

  //Set up the PDF uncertainty calculation:
  const int SUBSET = 0; //pdf subset
  if(verbose_ == true)std::cout << "initialising PDF Set" << std::endl;
//  LHAPDF::Verbosity verbose = LHAPDF::SILENT; //set to silent so it doesn't print out a load of stuff (see the include/LHAPDF.h for more)
//  LHAPDF::setVerbosity(verbose);
  const string NAME1 = "/vols/cms03/bm409/LHAPDF/share/lhapdf/cteq66.LHgrid"; //location of the pdf set
  const string NAME2 = "/vols/cms03/bm409/LHAPDF/share/lhapdf/MSTW2008nlo68cl.LHgrid"; //location of the pdf set
  const string NAME3 = "/vols/cms03/bm409/LHAPDF/share/lhapdf/NNPDF20_100.LHgrid";
  LHAPDF::setPDFPath("/vols/cms03/bm409/LHAPDF/share/lhapdf/");

  std::string pdfName1_ = "cteq61";
  // std::string pdfName2_ = "MSTW2008nlo68cl";
  const int pdfSubset = 0;
  LHAPDF::initPDFSet(1, pdfName1_, LHAPDF::LHGRID, pdfSubset);
  // LHAPDF::initPDFSet(2, pdfName2_, LHAPDF::LHGRID, pdfSubset);
      // LHAPDF::initPDFSet(2,NAME2);
  //    LHAPDF::initPDFSet(3,NAME3);



  //Set up the PDF uncertainty calculation:

}

void PDFPlottingOps::BookHistos() {


  //
  // BookHistArray( H_M0_M12_cteq66,
  //   "m0_m12_cteq66",
  //   ";m0;m12",
  //   xBins_,xLow_,xHigh_, //m0
  //   yBins_,yLow_,yHigh_, //m12
  //   zBins_,zLow_,zHigh_, //mChi
  //   45, 0, 1,false );

  BookHistArray( H_M0_M12_noweight,
    "m0_m12_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );
  BookHistArray( H_M0_M12_sb,
    "m0_m12_sb",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_ss,
    "m0_m12_ss",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_sg,
    "m0_m12_sg",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_gg,
    "m0_m12_gg",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_ll,
    "m0_m12_ll",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_nn,
    "m0_m12_nn",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_ng,
    "m0_m12_ng",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_ns,
    "m0_m12_ns",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_bb,
    "m0_m12_bb",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_tb,
    "m0_m12_tb",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    45, 0, 1,false );


  BookHistArray( H_M0_M12_sb_noweight,
    "m0_m12_sb_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );


  BookHistArray( H_M0_M12_ss_noweight,
    "m0_m12_ss_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );


  BookHistArray( H_M0_M12_sg_noweight,
    "m0_m12_sg_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );


  BookHistArray( H_M0_M12_gg_noweight,
    "m0_m12_gg_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );


  BookHistArray( H_M0_M12_ll_noweight,
    "m0_m12_ll_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );


  BookHistArray( H_M0_M12_nn_noweight,
    "m0_m12_nn_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );


  BookHistArray( H_M0_M12_ng_noweight,
    "m0_m12_ng_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );


  BookHistArray( H_M0_M12_ns_noweight,
    "m0_m12_ns_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );


  BookHistArray( H_M0_M12_bb_noweight,
    "m0_m12_bb_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );


  BookHistArray( H_M0_M12_tb_noweight,
    "m0_m12_tb_noweight",
    ";m0;m12",
    xBins_,xLow_,xHigh_,//m0
    yBins_,yLow_,yHigh_,//m12
    1, 0, 1,false );



  //
  // cout << " Histograms are now booked" << endl;

  // BookHistArray( H_M0_M12_MSTW2008,
  //    "m0_m12_MSTW2008",
  //    ";m0;m12",
  //    xBins_,xLow_,xHigh_, //m0
  //    yBins_,yLow_,yHigh_, //m12
  //    zBins_,zLow_,zHigh_, //mChi
  //    41, 0, 1,false );
  //
  // BookHistArray( H_M0_M12_NNPDF,
  //    "m0_m12_NNPDF",
  //    ";m0;m12",
  //    xBins_,xLow_,xHigh_, //m0
  //    yBins_,yLow_,yHigh_, //m12
  //    zBins_,zLow_,zHigh_, //mChi
  //    101, 0, 1,false );

  // BookHistArray( H_M0_M12_pdfweight,
  //    "m0_m12_pdfweight",
  //    ";m0;m12",
  //    xBins_,xLow_,xHigh_, //m0
  //    yBins_,yLow_,yHigh_, //m12
  //    100,0,10, //mChi
  //    sets_, 0, 1,false );

}


bool PDFPlottingOps::Process( Event::Data& ev ) {

  Double_t weight = ev.GetEventWeight();
  NLO::SUSYProcess process;

  double M0=0;
  double M12=0;
  double MChi =0;
  if(ev.M0.enabled()){
    M0 = ev.M0();
  }
  if(ev.MG.enabled()){
    M0 = ev.MG();
  }
  if(ev.M12.enabled()){
    M12 = ev.M12();
  }
  if(ev.MLSP.enabled()){
    M12 = ev.MLSP();
  }
  if(ev.MChi.enabled()){
    MChi = ev.MChi();
  }


  //NLO stuff: for the calculation of the NLO cross-section the processes are filled separately
  if((ev.M0.enabled() || ev.MG.enabled())){

    process = NLO::GetProcess(ev);

    Double_t NLOcrosssection = 0.; // if we dont find a NLO x section, fill with zero - this will help with debugging
    if(verbose_ )cout << " Leading order XC is " << weight << endl;
    std::map<std::pair<int,int> , std::vector<double> >::const_iterator nloXsec = M0_M12_NLO_.find(make_pair(int(M0),int(M12)));
    if(nloXsec != M0_M12_NLO_.end() && nloXsec->second.size() > process) {NLOcrosssection = nloXsec->second[process]; //if no valid kFactorFile has been given simply fill LO eventweight
      if(verbose_ )cout << " Event Weight is now set to xsection = " << nloXsec->second[process] << endl;
    }

  //now set up the baseline values with which to weight relative to:
    // LHAPDF::usePDFMember(2, 0);
    // double fx1Q0Other = LHAPDF::xfx(ev.genx1(), ev.genQ(), ev.genid1())/ev.genx1();
    // double fx2Q0Other = LHAPDF::xfx(ev.genx2(), ev.genQ(), ev.genid2())/ev.genx2();


    LHAPDF::usePDFMember(1, 0);
    double genpdf1 = LHAPDF::xfx(ev.genx1(), ev.genQ(), ev.genid1())/ev.genx1();
    double genpdf2 = LHAPDF::xfx(ev.genx2(), ev.genQ(), ev.genid2())/ev.genx2();



    // double pdfWeightOther = (fx1Q0Other*fx2Q0Other)/(fx1Q0*fx2Q0);


    if(verbose_ == true){
      std::cout << "pdf1: " << genpdf1 << std::endl;
      std::cout << "pdf2: " << genpdf2 << std::endl;
    }



        H_M0_M12_noweight[0]->Fill(M0,M12,1);
        switch(process){
          case NLO::nn:  H_M0_M12_nn_noweight[0]->Fill(M0,M12,1); break;
          case NLO::ns:  H_M0_M12_ns_noweight[0]->Fill(M0,M12,1); break;
          case NLO::ng:  H_M0_M12_ng_noweight[0]->Fill(M0,M12,1); break;
          case NLO::ss:  H_M0_M12_ss_noweight[0]->Fill(M0,M12,1); break;
          case NLO::ll:  H_M0_M12_ll_noweight[0]->Fill(M0,M12,1); break;
          case NLO::sb:  H_M0_M12_sb_noweight[0]->Fill(M0,M12,1); break;
          case NLO::tb:  H_M0_M12_tb_noweight[0]->Fill(M0,M12,1); break;
          case NLO::gg:  H_M0_M12_gg_noweight[0]->Fill(M0,M12,1); break;
          case NLO::bb:  H_M0_M12_bb_noweight[0]->Fill(M0,M12,1); break;
          case NLO::sg:  H_M0_M12_sg_noweight[0]->Fill(M0,M12,1); break;
          case NLO::NotFound: if(verbose_){cout << " DID NOT FIND A SUBPROCESS " << endl;} break;
        }



      const int NUMBER = LHAPDF::numberPDF(1);

      if(verbose_ == true)cout << " number " << NUMBER << endl;

      for (int n = 0; n < NUMBER + 1; ++n) {
        if(verbose_ == true)cout << "Set number: " << n << endl;
        LHAPDF::initPDF(n);
        double newpdf1 =  LHAPDF::xfx(ev.genx1(), ev.genQ(), ev.genid1())/ev.genx1();
        double newpdf2 =  LHAPDF::xfx(ev.genx2(), ev.genQ(), ev.genid2())/ev.genx2();
        double PDFUncWeight = (newpdf1/genpdf1)*(newpdf2/genpdf2);

        if(verbose_ == true)cout << " n " << n << " M0 " << M0  << " M12 " << M12  << " pdfweight " << PDFUncWeight << endl;


      // if(k==1)H_M0_M12_cteq66[n]  ->Fill(M0,M12,MChi,weight*PDFUncWeight);
      // if(k==2)H_M0_M12_MSTW2008[n]->Fill(M0,M12,MChi,weight*PDFUncWeight);
      // if(k==3)H_M0_M12_NNPDF[n]   ->Fill(M0,M12,MChi,weight*PDFUncWeight);
        if(verbose_ == true)cout << " m0 " << M0 << " m12 " << M12 << " nlocross " << NLOcrosssection << endl;
        switch(process){
          case NLO::nn: H_M0_M12_nn[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::ns: H_M0_M12_ns[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::ng: H_M0_M12_ng[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::ss: H_M0_M12_ss[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::ll: H_M0_M12_ll[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::sb: H_M0_M12_sb[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::tb: H_M0_M12_tb[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::gg: H_M0_M12_gg[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::bb: H_M0_M12_bb[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::sg: H_M0_M12_sg[n]->Fill(M0,M12,NLOcrosssection*PDFUncWeight); break;
          case NLO::NotFound: if(verbose_){cout << " DID NOT FIND A SUBPROCESS " << endl;} break;
        }
    }
  }
    return true;

  }





  std::ostream& PDFPlottingOps::Description( std::ostream& ostrm ) {
    ostrm << "PDF mSuGra scan 2d Plots ";
    return ostrm;
  }






