select * from titles
join publishers on titles.pub_id = publishers.pub_id
join titleauthor on titleauthor.title_id = titles.title_id 
join authors on authors.au_id = titleauthor.au_id ;

 


 



















