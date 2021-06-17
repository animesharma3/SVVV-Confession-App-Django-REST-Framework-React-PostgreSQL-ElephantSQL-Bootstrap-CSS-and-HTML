
const UserProfile = ({profile}) => {
    const profilePicStyle = {
        width: "100px",
        height: "100px",
        borderRadius: "50%",
    }
    return (
        <div className='card'>
            <div className="card-body">
            <div className="row">
                <img src="https://avatars.githubusercontent.com/u/48760865?v=4" style={profilePicStyle} className='col-md-5' alt="" />
                <div className="col-md-7 text-center">
                    <h5 className="">{profile.first_name + ' ' + profile.last_name}</h5>
                    <p className='text-secondary'>animesharma3</p>
                </div> 
            </div>
            </div>
        </div>
    )
}

export default UserProfile
