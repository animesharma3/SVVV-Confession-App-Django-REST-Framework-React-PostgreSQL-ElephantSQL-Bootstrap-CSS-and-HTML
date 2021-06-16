import Post from './Post'


const Posts = ({ confessions }) => {
    return (
        <div className='container'>
            <div className='posts'>
                {
                    confessions.map(
                        (confession) => (
                            <div className="post" key={parseInt(confession.id)}>
                                <Post confession={confession} />
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
