
const Post = ({ confession }) => {
    return (
        <>
            <div className="container card">
                <div className="card-body">
                    <h3 className="card-title">{confession.title}</h3>
                    <p className="card-text">{confession.text}</p>
                </div>
            </div>
        </>
    )
}

export default Post
