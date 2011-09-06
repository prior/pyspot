class Blog():
  """define the HubSpot blog object that we'll pass back to the user"""
  def __init__(self, blog_json):
    self.xml_parse(blog_json)
  
  def xml_parse(self, blog_json):
    self.guid = blog_json['guid']
    self.feed_url = blog_json['feedUrl']
    self.blog_title = blog_json['blogTitle']
    self.portal_id = blog_json['portalId']
    self.web_url = blog_json['webUrl']
  

class BlogComment():
  """defines the HubSpot Blog comment object"""
  
  def __init__(self, comment_xml):
    self.xml_parse(comment_xml)
  
  def xml_parse(self, xml):
    # Creating Nodes
    feedNode = xml.firstChild  # Feed node that wraps the whole XML.
    commentEntryNode = feedNode.childNodes[3]
    commentIdNode = commentEntryNode.childNodes[0]
    commentAuthorNode = commentEntryNode.childNodes[1]
    authorNameNode = commentAuthorNode.childNodes[0]
    authorEmailNode = commentAuthorNode.childNodes[1]
    authorUriNode = commentAuthorNode.childNodes[2]
    contentNode = commentEntryNode.childNodes[2]
    publishedNode = commentEntryNode.childNodes[3]
    userTokenNode = commentEntryNode.childNodes[6]
    judgeScoredNode = commentEntryNode.childNodes[7]
    if userTokenNode.firstChild:
      user_token = userTokenNode.childNodes[0].data
      self.set_user_token(user_token)
    else:
      pass
      
    if judgeScoredNode.firstChild:
      judge_scored_time = judgeScoredNode.childNodes[0].data
      self.set_judge_scored_time(judge_scored_time)
    else:
      pass
      
    isSpamNode = commentEntryNode.childNodes[8]
    
    # Drilling down to text and setting class variables
    self.comment_guid = commentIdNode.childNodes[0].data
    self.comment_author_name = authorNameNode.childNodes[0].data
    self.comment_author_email = authorEmailNode.childNodes[0].data
    self.comment_author_uri = authorUriNode.childNodes[0].data
    self.comment_content = contentNode.childNodes[0].data
    self.published_time = publishedNode.childNodes[0].data
    self.is_comment_spam = isSpamNode.childNodes[0].data
  

class BlogPost():
  """define the HubSpot Blog Post object that will get hydrated and passed back to the user"""
  def __init__(self, blog_post_json):
    self.parse_xml(blog_post_json)
  
  def parse_xml(self, xml):
    # Creating Nodes
    feedNode = xml.firstChild  # Feed node that wraps the whole XML.
    idNode = feedNode.firstChild  # id field
    blogTitleNode = feedNode.childNodes[1]  # Blog title field
    entryNode = feedNode.childNodes[2]
    postIdNode = entryNode.firstChild
    postTitle = entryNode.childNodes[1]
    postSummary = entryNode.childNodes[2]
    postContent = entryNode.childNodes[3]
    authorNode = entryNode.childNodes[4]
    postAuthorName = authorNode.firstChild
    postAuthorEmail = authorNode.childNodes[1]
    # skipped <link /> need to revisit
    updatedNode = entryNode.childNodes[6]
    publishedNode = entryNode.childNodes[7]
    portalIdNode = entryNode.childNodes[8]
    # Skipped blogGuid because it's redundant
    metaDescNode = entryNode.childNodes[10]
    metaKeywordNode = entryNode.childNodes[11]
    isDraftNode = entryNode.childNodes[12]
    sendNotifyNode = entryNode.childNodes[13]
    analyticsNode = entryNode.childNodes[14]
    postViewsNode = analyticsNode.childNodes[0]
    postCommentsNode = analyticsNode.childNodes[1]
    postLinksNode = analyticsNode.childNodes[2]
    
    # Drilling down to text and setting class variables
    self.blog_id = idNode.childNodes[0].data
    self.blog_title = blogTitleNode.childNodes[0].data
    self.post_id = postIdNode.childNodes[0].data
    self.post_title = postTitle.childNodes[0].data
    self.post_summary = postSummary.childNodes[0].data
    self.post_content = postContent.childNodes[0].data
    self.post_author_name = postAuthorName.childNodes[0].data
    self.post_author_email = postAuthorEmail.childNodes[0].data
    self.updated_time = updatedNode.childNodes[0].data
    self.published_time = publishedNode.childNodes[0].data
    self.portal_id = portalIdNode.childNodes[0].data
    if metaDescNode.firstChild:
      meta_desc = metaDescNode.childNodes[0].data
      self.set_meta_desc(meta_desc)
    else:
      pass
      
    if metaKeywordNode.firstChild:
      meta_keyword = metaKeywordNode.childNodes[0].data
      self.set_meta_keyword(meta_keyword)
    else:
      pass
      
    self.is_draft = isDraftNode.childNodes[0].data
    self.send_notify = sendNotifyNode.childNodes[0].data
    self.post_views = postViewsNode.childNodes[0].data
    self.post_comments = postCommentsNode.childNodes[0].data
    self.post_links = postLinksNode.childNodes[0].data
  

