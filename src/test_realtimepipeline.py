"""
This is the main file for testing realtime performance.

Copyright 2015 Markus Oberweger, ICG,
Graz University of Technology <oberweger@icg.tugraz.at>

This file is part of DeepPrior.

DeepPrior is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DeepPrior is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with DeepPrior.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
os.environ["THEANO_FLAGS"] = "device=gpu,floatX=float32"

import numpy
from data.dataset import NYUDataset, ICVLDataset
from net.poseregnet import PoseRegNetParams, PoseRegNet
from net.resnet import ResNetParams, ResNet
from net.scalenet import ScaleNetParams, ScaleNet
from util.realtimehandposepipeline import RealtimeHandposePipeline
from data.importers import ICVLImporter, NYUImporter, MSRA15Importer, MYImporter320, MYImporter
from util.cameradevice import FileDevice
from data.importers import DepthImporter
from util.cameradevice import RealsenseCameraDevice



__author__ = "Markus Oberweger <oberweger@icg.tugraz.at>"
__copyright__ = "Copyright 2015, ICG, Graz University of Technology, Austria"
__credits__ = ["Markus Oberweger"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Markus Oberweger"
__email__ = "oberweger@icg.tugraz.at"
__status__ = "Development"

if __name__ == '__main__':
    rng = numpy.random.RandomState(23455)

    # di = MSRA15Importer('../data/MSRA15/')
    # Seq2 = di.loadSequence('P1')
    # testSeqs = [Seq2]

    # di = ICVLImporter('../data/ICVL/')
    # Seq2 = di.loadSequence('test_seq_1')
    # testSeqs = [Seq2]

    # di = NYUImporter('../data/NYU/')
    # Seq2 = di.loadSequence('test_1')
    # testSeqs = [Seq2]

    # di = NYUImporter('../data/NYU/') # only read file names
    # Seq2 = di.loadFileNames('test_1')
    # testSeqs = Seq2

    # di = MYImporter320('/home/xuan/Code/RealSense2Sample/data/')  # only read file names
    # Seq2 = di.loadFileNames('data320')
    # testSeqs = Seq2

    di = MYImporter('/home/xuan/Code/RealSense2Sample/data/')  # only read file names
    Seq2 = di.loadFileNames('data640')
    testSeqs = Seq2

    # # MSRA model
    # poseNetParams = PoseRegNetParams(type=11, nChan=1, wIn=128, hIn=128, batchSize=8, numJoints=21, nDims=3)
    # poseNetParams.loadFile = "./eval/MSRA_network_prior_0.pkl"
    # comrefNetParams = ScaleNetParams(type=1, nChan=1, wIn=128, hIn=128, batchSize=8, resizeFactor=2, numJoints=1,
    #                                  nDims=3)
    # comrefNetParams.loadFile = "./eval/net_MSRA15_COM_AUGMENT.pkl"
    # # config = {'fx': 588., 'fy': 587., 'cube': (300, 300, 300)}
    # config = {'fx': 315.066, 'fy': 315.066, 'cube': (200, 200, 200)}
    # # config = {'fx': 630.131, 'fy': 630.131, 'cube': (250, 250, 250)}
    # # config = {'fx': 241.42, 'fy': 241.42, 'cube': (250, 250, 250)}
    # # config = {'fx': 224.5, 'fy': 230.5, 'cube': (300, 300, 300)}  # Creative Gesture Camera
    # rtp = RealtimeHandposePipeline(poseNetParams, config, di, verbose=False, comrefNet=comrefNetParams)

    # # # use filenames
    # filenames = []
    # for i in testSeqs[0].data:
    #     # print ("file names: ")
    #     # print (i.fileName)
    #     filenames.append(i.fileName)
    # dev = FileDevice(filenames, di)
    #
    # # use depth camera
    # rtp.processVideo(dev)


    # # NYU model
    # load trained network (NYU model)
    poseNetParams = ResNetParams(type=1, nChan=1, wIn=128, hIn=128, batchSize=8, numJoints=14, nDims=3)
    poseNetParams.loadFile = "./eval/NYU_network_prior.pkl"
    # poseNetParams.loadFile = "./eval/ICVL_network_prior.pkl"
    comrefNetParams = ScaleNetParams(type=1, nChan=1, wIn=128, hIn=128, batchSize=8, resizeFactor=2, numJoints=1, nDims=3)
    comrefNetParams.loadFile = "./eval/net_NYU_COM_AUGMENT.pkl"
    # comrefNetParams.loadFile = "./eval/net_ICVL_COM_AUGMENT.pkl"
    # config = {'fx': 588., 'fy': 587., 'cube': (300, 300, 300)}
    config = {'fx': 630.131, 'fy': 630.131, 'cube': (250,250,250)}
    # config = {'fx': 241.42, 'fy': 241.42, 'cube': (250, 250, 250)}
    # config = {'fx': 224.5, 'fy': 230.5, 'cube': (300, 300, 300)}  # Creative Gesture Camera
    rtp = RealtimeHandposePipeline(poseNetParams, config, di, verbose=False, comrefNet=comrefNetParams)

    #use filenames
    filenames = testSeqs
    dev = FileDevice(filenames,di)
    # rtp.processVideoThreaded(dev)

    rtp.processVideo(dev)


