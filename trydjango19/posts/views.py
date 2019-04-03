from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post



# ### 추가한부분 ########################################################
# def contact(request):
# 	# with open("/Users/sim_macbookpro/Desktop/File0.txt", 'r') as f:
# 	# 	data = f.readlines()
# 	# title_sub = []
# 	# results = []
# 	# title_sub2 = []
# 	# results2 = []
# 	# for title in data[:2]:
# 	# 	title_sub.append(title.strip())
# 	# results.append((" ".join(title_sub)).strip())
# 	# output1 = (" ".join(results)).strip()
# 	# for title2 in data[2:]:
# 	# 	title_sub2.append(title2.strip())
# 	# results2.append((" ".join(title_sub2)).strip())
# 	# output2 = (" ".join(results2)).strip()
#
# 	from gensim.models import Doc2Vec
# 	import pickle
# 	import gensim
#
# 	# with open("/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/for_03/train_corpus_pickle","rb") as fp:
# 	# 	train_corpus = pickle.load(fp)
# 	#
# 	model = Doc2Vec.load('/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/for_03/model_mecab_noun_79403')
# 	# model = gensim.models.doc2vec.Doc2Vec(tratravector_size=50, min_count=2, epochs=40)
#
# 	#
# 	# with open("/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/for_03/ranks_pickle","rb") as fp:
# 	# 	ranks = pickle.load(fp)
# 	#
# 	# with open("/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/for_03/second_ranks_pickle","rb") as fp:
# 	# 	second_ranks = pickle.load(fp)
#
#
# 	test_corpus = ['자동차','사고', '손해배상']
# 	inferred_vector = model.infer_vector(test_corpus)
# 	sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
#
# 	filenum = []
# 	for label, index in [('MOST', 0), ('SECOND', 1), ('THIRD', 2), ('THIRD', 3), ('THIRD', 4), ('THIRD', 5), ('THIRD', 6), ('THIRD', 7), ('THIRD', 8), ('THIRD', 9), ('THIRD', 10), ]:
# 		filenum.append(sims[index][0])
#
# 	posts = []
# 	for num in filenum:
# 		post_one = Post.objects.get(fileid = num)
# 		posts.append(post_one)
#
# 	return render(request, 'basic.html', {'posts':posts})
# #####################################################################


### 추가한부분 ########################################################
def contact(request):

	from gensim.models import Doc2Vec
	import pickle
	import gensim

	# with open("/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/for_03/train_corpus_pickle","rb") as fp:
	# 	train_corpus = pickle.load(fp)
	#
	model = Doc2Vec.load('/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/for_03/model_mecab_noun_79403')
	# model = gensim.models.doc2vec.Doc2Vec(tratravector_size=50, min_count=2, epochs=40)

	#
	# with open("/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/for_03/ranks_pickle","rb") as fp:
	# 	ranks = pickle.load(fp)
	#
	# with open("/Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/for_03/second_ranks_pickle","rb") as fp:
	# 	second_ranks = pickle.load(fp)

	test_corpus = ['자동차', '사고', '손해배상']
	inferred_vector = model.infer_vector(test_corpus)
	sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))

	filenum = []
	for label, index in [('MOST', 0), ('SECOND', 1), ('THIRD', 2), ('THIRD', 3), ('THIRD', 4), ('THIRD', 5),
						 ('THIRD', 6), ('THIRD', 7), ('THIRD', 8), ('THIRD', 9), ('THIRD', 10),('MOST', 11), ('SECOND', 12), ('THIRD', 13), ('THIRD', 14), ('THIRD', 15), ('THIRD', 16),
						 ('THIRD', 17), ('THIRD', 18), ('THIRD', 19), ('THIRD', 20), ('THIRD', 21), ]:
		filenum.append(sims[index][0])




	posts1 = []
	space = ['___________________________________________________________________________________________________________________________________________________________________']
	similar = ['유사도']
	space2 = ['______________________________________________________________________________________________________________________________________________________']

	for i, num in enumerate(filenum):
		with open("//Users/sim_macbookpro/projects/project_judical_precednet_not_py/download_j_precednet/jp_by_4000/total_txt/File"+ str(num) +".txt", 'r') as f:
			data = f.readlines()
		title_sub = []
		title_sub2 = []
		for title in data[:2]:
			title_sub.append(title.strip())
		for title2 in data[2:]:
			title_sub2.append(title2.strip())
		ranking = [str(i)+ '순위 : ']

		posts1.append((" ".join(similar + ranking + title_sub + space + title_sub2)).strip())

	return render(request, 'basic.html',{'content': posts1})


#####################################################################


def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list = Post.objects.all() #.order_by("-timestamp")

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(subtitle__icontains=query)
			).distinct()


	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset,
		"title": "인공지능 판례검색",
	"page_request_var": page_request_var
	}
	return render(request, "post_list.html", context)





def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)



def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")