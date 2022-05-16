from flask import render_template,redirect,url
from . import main

@main.route('/')
def index():
    
    all_category = PostCategory.get_categories()
    all_posts = Post.query.order_by('id').all()
    quote = get_quote()
    print(all_posts)
    
    title = 'Blog Post'
    return render_template('index.html',all_posts= all_posts, categories = all_category, title=title,quote=quote)

@main.route('/category/new-post/<int:id>')
def new_post(id):
    
    category = PostCategory.query.filter_by(id=id).first()

    
    return render_template('new_post.html')

@main.route('/categories/<int:id>')
def category(id):
    
    category = PostCategory.query.filter_by(id)
    
    posts = Post.get_posts(id)
    return render_template('category.html',posts = posts, category=category)
    
@main.route('/add/category')
def new_category():
    
    title = 'New Category'
    
    return render_template('new_category.html',title = title)

@main.route('/view-pitch/<int:id>')
def view_pitch(id):
    
    all_category = PostCategory.get_categories()
    posts = Post.query.get(id)
    
    return render_template('view-pitch.html')

@main.route('/write_comment/<int:id>')
def post_comment(id):
    
    title = 'post comment'
    posts = Post.query.filter_by(id=id).first()
    
    return render_template('post_comment.html', title = title)

@main.route('/user/uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/post/upvote/<int:id>&<int:vote_type>')
@login_required
def upvote(id,vote_type):
    votes = Votes.query.filter_by(user_id=current_user.id).all()
    print(f'The new vote is {votes}')
    to_str=f'{vote_type}:{current_user.id}:{id}'
    print(f'The current vote is {to_str}')

    if not votes:
        new_vote = Votes(vote=vote_type, user_id=current_user.id, pitches_id=id)
        new_vote.save_vote()
        print('YOU HAVE new VOTED')

    for vote in votes:
        if f'{vote}' == to_str:
            print('YOU CANNOT VOTE MORE THAN ONCE')
            break
        else:   
            new_vote = Votes(vote=vote_type, user_id=current_user.id, pitches_id=id)
            new_vote.save_vote()
            print('YOU HAVE VOTED')
            break
    return redirect(url_for('.view_post', id=id))   
    

    
    

    
    

        