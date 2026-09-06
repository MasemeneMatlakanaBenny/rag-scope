.. sectnum::
   :depth: 2

Topic Drift
===========

Topic-drift checks compare the principal topic words in two sets of documents.
They help identify whether retrieved knowledge, generated content, or user
queries have moved away from an expected topic distribution.

.. contents:: Section Navigation
   :local:
   :depth: 1

TopicSemanticContentDrift
-------------------------

``TopicSemanticContentDrift`` compares the topic distributions of reference
and analysis content documents. Use it when monitoring whether new content has
shifted away from an established reference corpus.

.. currentmodule:: ragscope.topic_drift

.. autoclass:: TopicSemanticContentDrift
   :members: detect_mismatching_topics, topic_word_drift, dice_coeff, braun_coeff, jaccard_coeff, overlap_coeff, tanimoto_coeff
   :exclude-members: ref_topic_distribution, analysis_topic_distribution, topic_words_dict, topic_words_dataframes
   :member-order: bysource

TopicContentQueryDrift
----------------------

``TopicContentQueryDrift`` compares the topic distributions of knowledge-base
content and user queries. Use it to assess whether queries remain aligned with
the topics represented in the knowledge base.

.. autoclass:: TopicContentQueryDrift
   :members: detect_mismatching_topics, topic_word_drift, dice_coeff, braun_coeff, jaccard_coeff, overlap_coeff, tanimoto_coeff
   :exclude-members: query_topic_distribution, content_topic_distribution, topic_words_dict, topic_words_dataframes
   :member-order: bysource
