#          SF BAY ACM TALK: HEAVY TAILED SELF REGULARIZATION IN DEEP NEURAL NETWORKS  

My Collaborator did a great job giving a talk on our research at the local [San Francisco Bay ACM](https://www.youtube.com/channel/UCkWtKo2KIRioGMysSeQC6gg)Meetup

Michael W. Mahoney UC Berkeley

Random Matrix Theory (RMT) is applied to analyze the weight matrices of Deep Neural Networks (DNNs), including both production quality, pre-trained models and smaller models trained from scratch. Empirical and theoretical results clearly indicate that the DNN training process itself implicitly implements a form of self-regularization, implicitly sculpting a more regularized energy or penalty landscape. In particular, the empirical spectral density (ESD) of DNN layer matrices displays signatures of traditionally-regularized statistical models, even in the absence of exogenously specifying traditional forms of explicit regularization. Building on relatively recent results in RMT, most notably its extension to Universality classes of Heavy-Tailed matrices, and applying them to these empirical results, we develop a theory to identify 5+1 Phases of Training, corresponding to increasing amounts of implicit self-regularization. For smaller and/or older DNNs, this implicit self-regularization is like traditional Tikhonov regularization, in that there appears to be a “size scale” separating signal from noise. For state-of-the-art DNNs, however, we identify a novel form of heavy-tailed self-regularization, similar to the self-organization seen in the statistical physics of disordered systems. This implicit self-regularization can depend strongly on the many knobs of the training process. In particular, by exploiting the generalization gap phenomena, we demonstrate that we can cause a small model to exhibit all 5+1 phases of training simply by changing the batch size. This demonstrates that—all else being equal—DNN optimization with larger batch sizes leads to less-well implicitly-regularized models, and it provides an explanation for the generalization gap phenomena. Joint work with Charles Martin of Calculation Consulting, Inc.

Bio: [https://www.stat.berkeley.edu/~mmahoney/](https://www.youtube.com/redirect?redir_token=EZGiaSsZjKMZ1fnzP0YjtazIdd98MTU1NDIzMjIzNkAxNTU0MTQ1ODM2&q=https%3A%2F%2Fwww.stat.berkeley.edu%2F~mmahoney%2F&event=video_description&v=ILV5Sc8WjPY)

Michael W. Mahoney is at the UCB in the Department of Statistics and at the International Computer Science Institute (ICSI). He works on algorithmic and statistical aspects of modern large-scale data analysis. Much of his recent research has focused on large-scale machine learning, including randomized matrix algorithms and randomized numerical linear algebra, geometric network analysis tools for structure extraction in large informatics graphs, scalable implicit regularization methods, and applications in genetics, astronomy, medical imaging, social network analysis, and internet data analysis. He received him PhD from Yale University with a dissertation in computational statistical mechanics. He has worked and taught at Yale University in the Math department, Yahoo Research, and Stanford University in the Math department. Among other things, he is on the national advisory committee of the Statistical and Applied Mathematical Sciences Institute (SAMSI), He was on the National Research Council’s Committee on the Analysis of Massive Data. He co-organized the Simons Institute’s fall 2013 program on the Theoretical Foundations of Big Data Analysis, and he runs the biennial MMDS Workshops on Algorithms for Modern Massive Data Sets. He is currently the lead PI for the NSF/TRIPODS-funded FODA (Foundations of Data Analysis) Institute at UC Berkeley. He holds several patents for work done at Yahoo Research and as Lead Data Scientist for Vieu Labs, Inc., a startup re-imagining consumer video for billions of users.

More information is available at [https://www.stat.berkeley.edu/~mmahoney/](https://www.youtube.com/redirect?redir_token=EZGiaSsZjKMZ1fnzP0YjtazIdd98MTU1NDIzMjIzNkAxNTU0MTQ1ODM2&q=https%3A%2F%2Fwww.stat.berkeley.edu%2F~mmahoney%2F&event=video_description&v=ILV5Sc8WjPY)

Long version of the paper (upon which the talk is based): [https://arxiv.org/abs/1810.01075](https://www.youtube.com/redirect?redir_token=EZGiaSsZjKMZ1fnzP0YjtazIdd98MTU1NDIzMjIzNkAxNTU0MTQ1ODM2&q=https%3A%2F%2Farxiv.org%2Fabs%2F1810.01075&event=video_description&v=ILV5Sc8WjPY)[http://www.meetup.com/SF-Bay-ACM/](https://www.youtube.com/redirect?redir_token=EZGiaSsZjKMZ1fnzP0YjtazIdd98MTU1NDIzMjIzNkAxNTU0MTQ1ODM2&q=http%3A%2F%2Fwww.meetup.com%2FSF-Bay-ACM%2F&event=video_description&v=ILV5Sc8WjPY)[http://www.sfbayacm.org/](https://www.youtube.com/redirect?redir_token=EZGiaSsZjKMZ1fnzP0YjtazIdd98MTU1NDIzMjIzNkAxNTU0MTQ1ODM2&q=http%3A%2F%2Fwww.sfbayacm.org%2F&event=video_description&v=ILV5Sc8WjPY)