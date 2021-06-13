import Post from './Post'


const Posts = ({ confessions }) => {
    return (
        <div className='container'>
            <div className='posts'>
                {
                    confessions.map(
                        (confession) => (
                            <div className="post">
                                <Post key={confession.id} confession={confession} />
                                <br />
                            </div>
                        )
                    )
                }
            </div>
        </div>
    )
}

export default Posts
