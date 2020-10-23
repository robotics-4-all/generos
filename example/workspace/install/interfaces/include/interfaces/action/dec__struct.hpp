// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:action/Dec.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__ACTION__DEC__STRUCT_HPP_
#define INTERFACES__ACTION__DEC__STRUCT_HPP_

#include <rosidl_generator_cpp/bounded_vector.hpp>
#include <rosidl_generator_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Dec_Goal __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Dec_Goal __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Dec_Goal_
{
  using Type = Dec_Goal_<ContainerAllocator>;

  explicit Dec_Goal_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->x1 = 0ll;
      this->x2 = 0.0;
    }
  }

  explicit Dec_Goal_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->x1 = 0ll;
      this->x2 = 0.0;
    }
  }

  // field types and members
  using _x1_type =
    int64_t;
  _x1_type x1;
  using _x2_type =
    double;
  _x2_type x2;

  // setters for named parameter idiom
  Type & set__x1(
    const int64_t & _arg)
  {
    this->x1 = _arg;
    return *this;
  }
  Type & set__x2(
    const double & _arg)
  {
    this->x2 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Dec_Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Dec_Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Dec_Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Dec_Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Dec_Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Dec_Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Dec_Goal
    std::shared_ptr<interfaces::action::Dec_Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Dec_Goal
    std::shared_ptr<interfaces::action::Dec_Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dec_Goal_ & other) const
  {
    if (this->x1 != other.x1) {
      return false;
    }
    if (this->x2 != other.x2) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dec_Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dec_Goal_

// alias to use template instance with default allocator
using Dec_Goal =
  interfaces::action::Dec_Goal_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Dec_Result __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Dec_Result __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Dec_Result_
{
  using Type = Dec_Result_<ContainerAllocator>;

  explicit Dec_Result_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->y = 0.0;
    }
  }

  explicit Dec_Result_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->y = 0.0;
    }
  }

  // field types and members
  using _y_type =
    double;
  _y_type y;

  // setters for named parameter idiom
  Type & set__y(
    const double & _arg)
  {
    this->y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Dec_Result_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Dec_Result_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Dec_Result_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Dec_Result_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_Result_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_Result_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_Result_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_Result_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Dec_Result_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Dec_Result_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Dec_Result
    std::shared_ptr<interfaces::action::Dec_Result_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Dec_Result
    std::shared_ptr<interfaces::action::Dec_Result_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dec_Result_ & other) const
  {
    if (this->y != other.y) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dec_Result_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dec_Result_

// alias to use template instance with default allocator
using Dec_Result =
  interfaces::action::Dec_Result_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

// Include directives for member types
// Member 'h'
#include "std_msgs/msg/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Dec_Feedback __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Dec_Feedback __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Dec_Feedback_
{
  using Type = Dec_Feedback_<ContainerAllocator>;

  explicit Dec_Feedback_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : h(_init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->yt = 0.0;
    }
  }

  explicit Dec_Feedback_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : h(_alloc, _init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->yt = 0.0;
    }
  }

  // field types and members
  using _h_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _h_type h;
  using _yt_type =
    double;
  _yt_type yt;

  // setters for named parameter idiom
  Type & set__h(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->h = _arg;
    return *this;
  }
  Type & set__yt(
    const double & _arg)
  {
    this->yt = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Dec_Feedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Dec_Feedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Dec_Feedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Dec_Feedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_Feedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_Feedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_Feedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_Feedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Dec_Feedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Dec_Feedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Dec_Feedback
    std::shared_ptr<interfaces::action::Dec_Feedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Dec_Feedback
    std::shared_ptr<interfaces::action::Dec_Feedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dec_Feedback_ & other) const
  {
    if (this->h != other.h) {
      return false;
    }
    if (this->yt != other.yt) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dec_Feedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dec_Feedback_

// alias to use template instance with default allocator
using Dec_Feedback =
  interfaces::action::Dec_Feedback_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/uuid__struct.hpp"
// Member 'goal'
#include "interfaces/action/dec__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Dec_SendGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Dec_SendGoal_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Dec_SendGoal_Request_
{
  using Type = Dec_SendGoal_Request_<ContainerAllocator>;

  explicit Dec_SendGoal_Request_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit Dec_SendGoal_Request_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _goal_type =
    interfaces::action::Dec_Goal_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__goal(
    const interfaces::action::Dec_Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Dec_SendGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Dec_SendGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Dec_SendGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Dec_SendGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_SendGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_SendGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_SendGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_SendGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Dec_SendGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Dec_SendGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Dec_SendGoal_Request
    std::shared_ptr<interfaces::action::Dec_SendGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Dec_SendGoal_Request
    std::shared_ptr<interfaces::action::Dec_SendGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dec_SendGoal_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dec_SendGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dec_SendGoal_Request_

// alias to use template instance with default allocator
using Dec_SendGoal_Request =
  interfaces::action::Dec_SendGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Dec_SendGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Dec_SendGoal_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Dec_SendGoal_Response_
{
  using Type = Dec_SendGoal_Response_<ContainerAllocator>;

  explicit Dec_SendGoal_Response_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit Dec_SendGoal_Response_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  // field types and members
  using _accepted_type =
    bool;
  _accepted_type accepted;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Dec_SendGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Dec_SendGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Dec_SendGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Dec_SendGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_SendGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_SendGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_SendGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_SendGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Dec_SendGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Dec_SendGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Dec_SendGoal_Response
    std::shared_ptr<interfaces::action::Dec_SendGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Dec_SendGoal_Response
    std::shared_ptr<interfaces::action::Dec_SendGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dec_SendGoal_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dec_SendGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dec_SendGoal_Response_

// alias to use template instance with default allocator
using Dec_SendGoal_Response =
  interfaces::action::Dec_SendGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

namespace interfaces
{

namespace action
{

struct Dec_SendGoal
{
  using Request = interfaces::action::Dec_SendGoal_Request;
  using Response = interfaces::action::Dec_SendGoal_Response;
};

}  // namespace action

}  // namespace interfaces

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Dec_GetResult_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Dec_GetResult_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Dec_GetResult_Request_
{
  using Type = Dec_GetResult_Request_<ContainerAllocator>;

  explicit Dec_GetResult_Request_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_init)
  {
    (void)_init;
  }

  explicit Dec_GetResult_Request_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Dec_GetResult_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Dec_GetResult_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Dec_GetResult_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Dec_GetResult_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_GetResult_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_GetResult_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_GetResult_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_GetResult_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Dec_GetResult_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Dec_GetResult_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Dec_GetResult_Request
    std::shared_ptr<interfaces::action::Dec_GetResult_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Dec_GetResult_Request
    std::shared_ptr<interfaces::action::Dec_GetResult_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dec_GetResult_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dec_GetResult_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dec_GetResult_Request_

// alias to use template instance with default allocator
using Dec_GetResult_Request =
  interfaces::action::Dec_GetResult_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

// Include directives for member types
// Member 'result'
// already included above
// #include "interfaces/action/dec__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Dec_GetResult_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Dec_GetResult_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Dec_GetResult_Response_
{
  using Type = Dec_GetResult_Response_<ContainerAllocator>;

  explicit Dec_GetResult_Response_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : result(_init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit Dec_GetResult_Response_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : result(_alloc, _init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _status_type =
    int8_t;
  _status_type status;
  using _result_type =
    interfaces::action::Dec_Result_<ContainerAllocator>;
  _result_type result;

  // setters for named parameter idiom
  Type & set__status(
    const int8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__result(
    const interfaces::action::Dec_Result_<ContainerAllocator> & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Dec_GetResult_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Dec_GetResult_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Dec_GetResult_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Dec_GetResult_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_GetResult_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_GetResult_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_GetResult_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_GetResult_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Dec_GetResult_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Dec_GetResult_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Dec_GetResult_Response
    std::shared_ptr<interfaces::action::Dec_GetResult_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Dec_GetResult_Response
    std::shared_ptr<interfaces::action::Dec_GetResult_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dec_GetResult_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dec_GetResult_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dec_GetResult_Response_

// alias to use template instance with default allocator
using Dec_GetResult_Response =
  interfaces::action::Dec_GetResult_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

namespace interfaces
{

namespace action
{

struct Dec_GetResult
{
  using Request = interfaces::action::Dec_GetResult_Request;
  using Response = interfaces::action::Dec_GetResult_Response;
};

}  // namespace action

}  // namespace interfaces

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__struct.hpp"
// Member 'feedback'
// already included above
// #include "interfaces/action/dec__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Dec_FeedbackMessage __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Dec_FeedbackMessage __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Dec_FeedbackMessage_
{
  using Type = Dec_FeedbackMessage_<ContainerAllocator>;

  explicit Dec_FeedbackMessage_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    feedback(_init)
  {
    (void)_init;
  }

  explicit Dec_FeedbackMessage_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    feedback(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _feedback_type =
    interfaces::action::Dec_Feedback_<ContainerAllocator>;
  _feedback_type feedback;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__feedback(
    const interfaces::action::Dec_Feedback_<ContainerAllocator> & _arg)
  {
    this->feedback = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Dec_FeedbackMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Dec_FeedbackMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Dec_FeedbackMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Dec_FeedbackMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_FeedbackMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_FeedbackMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Dec_FeedbackMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Dec_FeedbackMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Dec_FeedbackMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Dec_FeedbackMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Dec_FeedbackMessage
    std::shared_ptr<interfaces::action::Dec_FeedbackMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Dec_FeedbackMessage
    std::shared_ptr<interfaces::action::Dec_FeedbackMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dec_FeedbackMessage_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->feedback != other.feedback) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dec_FeedbackMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dec_FeedbackMessage_

// alias to use template instance with default allocator
using Dec_FeedbackMessage =
  interfaces::action::Dec_FeedbackMessage_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

#include "action_msgs/srv/cancel_goal.hpp"
#include "action_msgs/msg/goal_info.hpp"
#include "action_msgs/msg/goal_status_array.hpp"

namespace interfaces
{

namespace action
{

struct Dec
{
  /// The goal message defined in the action definition.
  using Goal = interfaces::action::Dec_Goal;
  /// The result message defined in the action definition.
  using Result = interfaces::action::Dec_Result;
  /// The feedback message defined in the action definition.
  using Feedback = interfaces::action::Dec_Feedback;

  struct Impl
  {
    /// The send_goal service using a wrapped version of the goal message as a request.
    using SendGoalService = interfaces::action::Dec_SendGoal;
    /// The get_result service using a wrapped version of the result message as a response.
    using GetResultService = interfaces::action::Dec_GetResult;
    /// The feedback message with generic fields which wraps the feedback message.
    using FeedbackMessage = interfaces::action::Dec_FeedbackMessage;

    /// The generic service to cancel a goal.
    using CancelGoalService = action_msgs::srv::CancelGoal;
    /// The generic message for the status of a goal.
    using GoalStatusMessage = action_msgs::msg::GoalStatusArray;
  };
};

typedef struct Dec Dec;

}  // namespace action

}  // namespace interfaces

#endif  // INTERFACES__ACTION__DEC__STRUCT_HPP_
